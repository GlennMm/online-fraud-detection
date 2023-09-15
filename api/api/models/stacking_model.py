from os import getcwd
import pandas as pd, tensorflow as tf, xgboost as xgb, lightgbm as lgb
import pickle, dill
from sklearn import metrics
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.preprocessing import RobustScaler
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, Activation
from tensorflow.keras.models import Sequential, Model
from keras import activations
from tensorflow.keras import regularizers
from tensorflow.keras.optimizers import Adam
from imblearn.under_sampling import RandomUnderSampler
from tensorflow.python.keras.layers import deserialize, serialize
from tensorflow.python.keras.saving import saving_utils

stack = None

get_neural_network = None

def get_all_categorical_features():
    features = [
        'ProductCD',
        'addr1', 
        'addr2',
        'P_emaildomain',
        'R_emaildomain',
        'DeviceType',
        'DeviceInfo',
    ]
    for i in range(1,7):
        features.append(f'card{i}')
    for i in range(1,10):
        features.append(f'M{i}')
    for i in range(12,39):
        features.append(f'id_{i}')
    return features


def correcting_data_types(data, features):
    for i in data:
        if i in features:
            data[i] = data[i].astype("string")
        else:
            data[i] = pd.to_numeric(data[i])
    return data


def fill_missing_values(data):
    for column in  data:
        if data[column].dtype.name == 'string':
            data[column].fillna('not available', inplace=True)
        else:
            mean = data[column].mean()
            if str(mean) == 'nan':
                data[column].fillna(0, inplace=True)
            else:
                data[column].fillna(mean, inplace=True)
    return data


def label_encode_categorical_features(data, features):
    encoder = preprocessing.LabelEncoder()
    for category in features:
        data[category] = encoder.fit_transform(data[category])
    return data


def cleaning_data(data, categorical_features):
    data = correcting_data_types(data=data, features=categorical_features)
    data = fill_missing_values(data=data)
    data = label_encode_categorical_features(data, categorical_features)
    # na_cols = [col for col in data.columns if data[col].isna().unique()[0] == True and len(data[col].isna().unique()) == 1]
    # data = data.drop(na_cols, axis=1)
    return data


def sample_and_scale_and_train_test_split(dataset):
    rus = RandomUnderSampler()
    std = RobustScaler()

    x_sampled, y_sampled = rus.fit_resample(dataset.drop(['isFraud'], axis=1), dataset['isFraud'])
    x_std = std.fit_transform(x_sampled)

    return train_test_split(x_std, y_sampled, shuffle=True, test_size=.3)


def get_neural_network():    
    l1=0.0000001
    l2=0.0000001
    dropout=0.05
    epochs = 100
    
    model = Sequential()
    model.add(Dense(100, activation=activations.linear, input_shape = (431,), activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))

    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(100, activation=activations.linear, activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))

    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(100, activation=activations.linear, activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))


    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(50, activation=activations.linear, activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))

    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(1, activation=activations.sigmoid))

    model.compile(optimizer=Adam(), loss=tf.keras.losses.logcosh, metrics=['accuracy'])

    return model


def clean(data):
    return cleaning_data(data, get_all_categorical_features())

def train_stack_model(data):
    print('Training the model')
    data = clean(data)
    x_train, x_test, y_train, y_test = sample_and_scale_and_train_test_split(data)
    stack.fit(x_train, y_train)
    y_pred = stack.predict(x_test)
    return {
        'f1': metrics.f1_score(y_test, y_pred),
        'accuracy': metrics.accuracy_score(y_test, y_pred),
        'precision': metrics.precision_score(y_test, y_pred),
        'recall': metrics.recall_score(y_test, y_pred),
    }

def test_stack_model(data):
    data = clean(data)
    y_test = data['isFraud']
    y_pred = stack.predict(data.drop(['isFraud'], axis=1))
    result = {
        'f1': metrics.f1_score(y_test, y_pred),
        'accuracy': metrics.accuracy_score(y_test, y_pred),
        'precision': metrics.precision_score(y_test, y_pred),
        'recall': metrics.recall_score(y_test, y_pred),
    }
    return result

def single_prediction(data):
    data = clean(data)
    return stack.predict(data)

def batch_prediction(data):
    data = clean(data)
    return stack.predict(data)
    

# with open(f'{getcwd()}/api/api/saved_model/stack_model.pkl', 'rb') as file:
stack = pickle.load(open(f'{getcwd()}/api/api/saved_model/stack_model.pkl', 'rb'))
