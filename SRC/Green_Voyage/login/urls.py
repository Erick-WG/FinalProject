from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.signIn, name="login"),
    path('createAccount/', views.signUp, name="signUp"),
    path('logout/', views.signOut, name="logout"),

]
