from django.shortcuts import render, redirect

# importing generic views.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#importing our custom form.
# from .forms import PostForm, EditForm
# importing out models
from .models import Destination, Activity
#importing our lazy folder for redirecting successful links.
from django.urls import reverse_lazy



# Home view class.
class HomeView(ListView):
    model = Destination
    template_name = 'home.html'
    context_object_name = 'destinations'

# Destinations view class.
class DestinationsView(DetailView):
    model = Destination
    template_name = 'destinations.html'
    context_object_name = 'destination'




















