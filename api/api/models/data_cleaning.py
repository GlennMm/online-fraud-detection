import pandas as pd
from sklearn.preprocessing import LabelEncoder


class CleanData:

    def __get_all_categorical_features(self):
        features = [
            'ProductCD',
            'addr1',
            'addr2',
            'P_emaildomain',
            'R_emaildomain',
            'DeviceType',
            'DeviceInfo',
        ]
        for i in range(1, 7):
            features.append(f'card{i}')
        for i in range(1, 10):
            features.append(f'M{i}')
        for i in range(12, 39):
            features.append(f'id_{i}')
        return features

    def __correcting_data_types(self, data, features):
        for i in data:
            if i in features:
                data[i] = data[i].astype("string")
            else:
                data[i] = pd.to_numeric(data[i])
        return data

    def __fill_missing_values(self, data):
        for column in data:
            if data[column].dtype.name == 'string':
                data[column].fillna('not available', inplace=True)
            else:
                mean = data[column].mean()
                if str(mean) == 'nan':
                    data[column].fillna(0, inplace=True)
                data[column].fillna(mean, inplace=True)
        return data

    def __cleaning_data(self, data, features):
        data = self.__correcting_data_types(data=data, features=self.__get_all_categorical_features())
        data = self.__fill_missing_values(data=data)
        data.drop(features, inplace=True, axis=1)
        return data

    def __label_encode_categorical_features(self, data, features):
        encoder = LabelEncoder()
        for category in features:
            data[category] = encoder.fit_transform(data[category])
        return data

    def clean(self, data):
        data = self.__cleaning_data(data, ['TransactionID', 'TransactionDT'])
        data = self.__label_encode_categorical_features(data, self.__get_all_categorical_features())
        return data
