from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import User
import json
from django.contrib.auth import authenticate
import logging
logger = logging.getLogger(__name__)


# Create your views here.

def index(self):
    return JsonResponse({"message": "Hello"})


def user_registration(request):
    data = json.loads(request.body)
    try:

        output = User.objects.create_user(username=data.get("username"), password=data.get("password"),
                                     email=data.get("email"), location=data.get("location"))
        print(output)
        print(request.body)
        return JsonResponse({'message': 'user Created'})
    except Exception as e:
        logger.exception(e)
        return JsonResponse({'message': f'{e}'})


def login_request(request):
    data = json.loads(request.body)
    try:

        if request.method == 'POST':
            username = data.get('username')
            password = data.get('password')
            user_list = authenticate(username=username, password=password)
            print(user_list)
            if not user_list:
                return JsonResponse({'mesaage': 'You entered wrong credentials'})

            return JsonResponse({'message': f'{username}:   logged in successfully'})

        elif request.method != 'POST':
            return JsonResponse({'message': 'Please Check Your Request Method'})
    except Exception as e:
        logger.exception(e)
        return JsonResponse({'message': f'{e}'})


# def user_deletion(request):
#     try:
#
#         data = json.loads(request.body)
#         user = User.objects.get(id=data.get('id'))
#         user.delete()
#         return JsonResponse({'message': 'user record deleted'})
#     except Exception as e:
#         return JsonResponse({'message': f'{e}'})
