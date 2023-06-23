from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CreateUserView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    # def (function for user management, login for users and admins.)
    success_url = reverse_lazy('dashboard')














