from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin/', views.signin, name="login"),
    path('createAccount/', views.signup, name="signUp"),
    path('signout/', views.signout, name="logout"),

]
