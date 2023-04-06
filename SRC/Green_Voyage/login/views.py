from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm()(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'template/signup.html', {'form': form}) #, {'form': form} was inside parentheses

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm()(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = AuthenticationForm()
    return render(request, 'template/signin.html', {'form': form}) #, {'form': form} was inside parentheses

@login_required
def home(request):
    return render(request, 'template/index.html')

@login_required
def signout(request):
    logout(request)
    return render(request, 'template/userac.html')
















