from django.urls import path
from . import views 

urlpatterns = [ 
    path("login", views.users_login),
    path("getcaptcha", views.users_captcha),
    path("register", views.users_register),
]