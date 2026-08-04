import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from Loginify import models

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, world!")


def _get_request_data(request):
    if request.content_type == "application/json":
        try:
            return json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return {}
    return request.POST


@csrf_exempt
def signup_view(request):
    if request.method == "GET":
        return render(request, "loginify/signup.html")

    if request.method == "POST":
        data = _get_request_data(request)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            if request.content_type == "application/json":
                return JsonResponse({"error": "username, email, and password are required"}, status=400)
            return JsonResponse({"error": "username, email, and password are required"}, status=400)

        if models.UserDetails.objects.filter(email=email).exists():
            if request.content_type == "application/json":
                return JsonResponse({"error": "email already exists"}, status=400)
            return JsonResponse({"error": "email already exists"}, status=400)

        models.UserDetails.objects.create(username=username, email=email, password=password)

        if request.content_type == "application/json":
            return JsonResponse({"message": "Signup successful"}, status=201)

        messages.success(request, "Signup successful. Please login now.")
        return redirect("login")

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == "GET":
        return render(request, "loginify/login.html")

    if request.method == "POST":
        data = _get_request_data(request)
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            if request.content_type == "application/json":
                return JsonResponse({"error": "email and password are required"}, status=400)
            return JsonResponse({"error": "email and password are required"}, status=400)

        user = models.UserDetails.objects.filter(email=email, password=password).first()

        if not user:
            if request.content_type == "application/json":
                return JsonResponse({"error": "Invalid email or password"}, status=401)
            return JsonResponse({"error": "Invalid email or password"}, status=401)

        if request.content_type == "application/json":
            return JsonResponse({"message": f"Welcome {user.username}!"}, status=200)

        messages.success(request, f"Welcome {user.username}!")
        return render(request, "loginify/success.html", {"username": user.username})

    return JsonResponse({"error": "Method not allowed"}, status=405)


def get_all_users(request):
    if request.method == "GET":
        users = list(models.UserDetails.objects.values("username", "email"))
        return JsonResponse({"users": users}, status=200)
    return JsonResponse({"error": "Method not allowed"}, status=405)


def get_user_by_email(request, email):
    if request.method == "GET":
        try:
            user = models.UserDetails.objects.get(email=email)
            return JsonResponse({"Username": user.username, "Email": user.email}, status=200)
        except models.UserDetails.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def update_user(request, email):
    if request.method == "GET":
        return render(request, "loginify/update.html")

    if request.method == "PUT":
        try:
            data = json.loads(request.body.decode("utf-8"))
            user = models.UserDetails.objects.get(email=email)
            user.username = data.get("username", user.username)
            user.password = data.get("password", user.password)
            user.save()
            return JsonResponse({"message": "User updated successfully"}, status=200)
        except models.UserDetails.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def delete_user(request, email):
    if request.method == "DELETE":
        try:
            user = models.UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({"message": "User deleted successfully"}, status=200)
        except models.UserDetails.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

    return JsonResponse({"error": "Method not allowed"}, status=405)