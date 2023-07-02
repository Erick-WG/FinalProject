from django.shortcuts import render, redirect

# importing generic views.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# importing our custom form.
# from .forms import DestinationCollectionForm, ActivityCreationForm
# importing out models
from .models import Destination, Activity
#importing our lazy folder for redirecting successful links.
from django.urls import reverse_lazy



# Home view class.
class HomeView(ListView):
    model = Destination
    template_name = 'index.html'
    # context_object_name = 'destinations'

# Destinations view class.
class DestinationsView(ListView):
    model = Destination
    template_name = 'destinations.html'
    # success_url = reverse_lazy('destinations')
    # context_object_name = 'destination'

# businesses can create destinations the provide touring to.
class CreateDestination(CreateView):
    model = Destination
    template_name = "create_destination.html"
    # form_class = DestinationCollectionForm


class CreateActivity(CreateView):
    model = Activity
    template_name = 'create_activity.html'
    # form_class = ActivityCreationForm


class DestinationsDeleteView(DeleteView):
    model = Destination
    template_name = 'delete_destination.html'
    success_url = reverse_lazy('home')
















