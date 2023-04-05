from django.shortcuts import HttpResponse
from django.shortcuts import render

def home (request):
    return render(request, "login/index.html")
def signUp (request):
    return render(request, "login/signup.html")


def signIn (request):
    return render(request, "login/login.html")


def signOut (request):
    return render(request, "login/logout.html")















