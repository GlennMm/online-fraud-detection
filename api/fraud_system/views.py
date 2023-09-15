from django.http.response import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def login(request, *args, **kwargs):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if not user:
            return JsonResponse(
                data = {
                    'error': True,
                    'message': 'Login failed'
                },
                status_code=400
            )    
        else:
            return JsonResponse(
                data = {
                    'username': user.user_name,
                },
                status_code=200
            )
    else:
        return JsonResponse(
            data = {
                'error': True,
                'message': 'Method not allowed'
            }
        )


def signup(request, *args, **kwargs):
    if request.method == "POST":
        user = User.objects.create_user(request.POST['username'], '', request.POST['password'])
        if not user:
            return JsonResponse(
                data = {
                    'error': True,
                    'message': 'Signup failed'
                },
                status_code=400
            )    
        else:
            return JsonResponse(
                data = {
                    'username': user.user_name,
                    'message': 'You have successfulyy signed up'
                },
                status_code=200
            )
    else:
        return JsonResponse(
            data = {
                'error': True,
                'message': 'Method not allowed'
            }
        )



def get_statistics(request, *args, **kwargs):
    response = {
        
    }
    return JsonResponse(
        data = response,
        status_code=200
    )