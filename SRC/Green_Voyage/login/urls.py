from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login_view"),
    path('signout/', views.signout, name="signout"),
    path('MyAccount/',views.user_view, name="user_view"),
]
