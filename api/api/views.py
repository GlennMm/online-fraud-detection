import pandas as pd

from api.models.fraud_detection_model import OnlineFraudDetection
from django.http.response import JsonResponse
from os import getcwd
from sklearn.metrics import accuracy_score, precision_score, f1_score
from rest_framework.decorators import api_view

from .models.stacking_model import cleaning_data, train_stack_model, test_stack_model, batch_prediction, single_prediction, stack

# model = OnlineFraudDetection()
# model.load_data(path)
# model.clean_data()
# model.train_model()
path = f'{getcwd()}/notebooks/data/system/test.csv'

init_data = pd.read_csv(path)
cols = init_data.drop(['isFraud'], axis=1).columns
# test_result = train_stack_model(init_data)

def load_data(path, predict=False):
    data = pd.read_csv(path, index_col='TransactionID')
    try:
        data.drop(['TransactionDT'], axis=1, inplace=True)
        if(predict):
            data.drop(['isFraud' ,'Unnamed: 0'], axis=1, inplace=True)
    except:
        pass
    return data

@api_view(['GET', 'POST'])
def train(request):
    file = request.FILES.get('dataset')
    result = train_stack_model(load_data(file))
    return JsonResponse(data=result, status=200)

@api_view(['GET', 'POST'])
def test(request):
    file = request.FILES.get('dataset')
    result = test_stack_model(load_data(file))
    return JsonResponse(data=result, status=200)

@api_view(['GET', 'POST'])
def predict(request):
    rec = request.POST.get('record').split(',')
    # print(rec)
    data = pd.DataFrame(data=[rec], columns=cols)
    data = data.drop(['TransactionID', 'TransactionDT'], axis=1)
    # if (hasattr(stack.classifier, 'classes_')):
    # print(rec.pop(0))
    # data.drop(['TransactionDT'], axis=1, inplace=True)
    # data.drop(['isFraud'], axis=1, inplace=True)
    # print(data)
    classification = single_prediction(data=data)
    result = {
        'classification': float(classification[0])
    }
    return JsonResponse(data=result, status=200)


@api_view(['GET', 'POST'])
def predict_batch(request):
    data = load_data(request.FILES.get('dataset'), predict=True)
    prediction = batch_prediction(data=data)
    fraud_count = len(prediction[prediction == 1])
    non_fraud_count = len(prediction[prediction == 0])
    clean = 'Yes' if fraud_count > 0 else 'No'
    result = {
        'fraud': {
            'count': fraud_count,
            'precentage': float(fraud_count/len(prediction))
        },
        'non_fraud': {
            'count': non_fraud_count,
            'precentage': float(non_fraud_count/len(prediction))
        },
        'clean': clean,
    }
    return JsonResponse(data=result, status=200)



@api_view(['GET', 'POST'])
def get_state(request):
    result = {
        'trained': hasattr(stack.classifier, 'classes_')
    }
    return JsonResponse(data=result, status=200)