import json
from email import message
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            user = User.objects.get(username=username)
            if authenticate(username=user.username, password=password) is not None:
                print("user logged in")
                message = "password is correct"
                status = "success"
                response = {"message": message,
                            "status": status}
                return JsonResponse(response)
            else:
                message = "passwords do not match"
                status = "failed"
                response = {"message": message,
                            "status": status}
                return JsonResponse(response)
        else:
            message = "user does not exist"
            status = "failed"
            response = {"message": message,
                        "status": status}
            return JsonResponse(response)