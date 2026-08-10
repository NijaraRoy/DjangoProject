import json
from math import e
import re
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from Loginify import models
from Loginify.serializers import UserDetailsModelSerializer
from rest_framework.parsers import JSONParser
from .forms import LoginForm, SignupForm
from .models import UserDetails
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, world!")

'''
Authentication views for user signup and login
'''
def signup_view(request):
    if request.method == "GET":
        return render(request, "loginify/signup.html", {"form": SignupForm()})

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()

            messages.success(request, "Signup successful. Please login now.")
            return redirect("login")

        return render(request, "loginify/signup.html", {"form": form}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


def login_view(request):
    if request.method == "GET":
        return render(request, "loginify/login.html", {"form": LoginForm()})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = UserDetails.objects.filter(email=email).first()

            if user and check_password(password, user.password):
                messages.success(request, f"Welcome {user.username}!")
                return render(request, "loginify/success.html", {"username": user.username})

            form.add_error(None, "Invalid email or password")
            return render(request, "loginify/login.html", {"form": form}, status=401)

        return render(request, "loginify/login.html", {"form": form}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)



'''
CRUD Operations for UserDetails model
'''

@csrf_exempt
def get_all_users(request):
    try:
        users_data = models.UserDetails.objects.all()
    except:
        data = {
            "message": "No users found, Sorry!",
            "status": 404
        }
        return JsonResponse(data, status=404)

    if request.method == "GET":
        all_users_serialized = UserDetailsModelSerializer(users_data, many=True).data
        return JsonResponse({"users": all_users_serialized},safe=False, status=200)
    
    elif request.method == "POST": #Add a new user
        input_data = JSONParser().parse(request)
        user_data_serialized = UserDetailsModelSerializer(data=input_data)
        
        if user_data_serialized.is_valid():
            user_data_serialized.save()
            return JsonResponse(user_data_serialized.data, status=201)
        else:
            return JsonResponse(user_data_serialized.errors, status=400)
        
        
@csrf_exempt    
def get_user_by_email(request, email):   
    
    try:
        user_data = models.UserDetails.objects.get(email=email)
    except:
        data = {
            "message": "User not found, Sorry!",
            "status": 404
        }
        return JsonResponse(data, status=404)
    
    if request.method == "GET":
        single_user_serialized = UserDetailsModelSerializer(user_data).data
        return JsonResponse({"user": single_user_serialized}, safe=False)
    
    elif request.method == "PUT":
        input_data = JSONParser().parse(request)
        user_data_serialized = UserDetailsModelSerializer(user_data, data=input_data)
        if user_data_serialized.is_valid():
            user_data_serialized.save()
            return JsonResponse(user_data_serialized.data, status=202)
        else:
            return JsonResponse(user_data_serialized.errors, status=400)
        
    elif request.method == "DELETE":
        user_data.delete()
        data = {
            "message": "User deleted successfully",
            "status": 204
        }
        return JsonResponse(data)
    