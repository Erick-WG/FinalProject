from django.urls import path
from .views import HomeView, DestinationsView

urlpatterns = [
    # creating our custom app urls.
    path('',HomeView.as_view(), name = 'home'),
    path('Destinations/<int:pk>', DestinationsView.as_view(), name = 'destinations'),

]
