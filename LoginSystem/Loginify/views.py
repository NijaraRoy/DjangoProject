from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from Loginify import models

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, world!")

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if models.UserDetails.objects.filter(email=email).exists():
            return JsonResponse({"error": "email already exists"}, status=400)

        models.UserDetails.objects.create(username=username, email=email, password=password)
        messages.success(request, "Signup successful. Please login now.")
        return redirect("login")

    return render(request, "loginify/signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = models.UserDetails.objects.filter(email=email, password=password).first()
        if not user:
            return JsonResponse({"error": "Invalid email or password"}, status=401)
        messages.success(request, f"Welcome {user.username}!")
        return render(request, "loginify/success.html", {"username": user.username})

    return render(request, "loginify/login.html")