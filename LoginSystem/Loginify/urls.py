"""
URL configuration for LoginSystem project.
"""

from django.contrib import admin
from django.urls import path, include
from Loginify import views

urlpatterns = [
    path("hello/", views.hello_world, name="hello_world"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("users/", views.get_all_users, name="get_all_users"),
    path("user/<str:email>/", views.get_user_by_email, name="get_user_by_email"),
    path("user/update/<str:email>/", views.update_user, name="update_user"),
    path("user/delete/<str:email>/", views.delete_user, name="delete_user"),
]