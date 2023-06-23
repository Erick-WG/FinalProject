from django.urls import path
from .views import HomeView, DestinationsView, CreateDestination, DestinationsDeleteView, CreateActivity # , ActivityView

urlpatterns = [
    # creating our custom app urls.
    path('',HomeView.as_view(), name = 'home'),
    path('create_Destinations/', CreateDestination.as_view(), name = 'create_destinations'),
    path('destinations/<int:pk>', DestinationsView.as_view(), name = 'destinations'),
    path('delete_destinations/<int:pk>', DestinationsDeleteView.as_view(), name = 'delete_destinations'),
    # # create a model, template for destination/activity and it's model.having both qualities for the destination and activity fields as foreign keys.
    # # let activities to also be accessed by slugify.
    # path('destinations/<int:pk>/activity/', ActivityView.as_view(), name = 'destinations_activity'),
    # path('activity/', ActivityView.as_view(), name = 'activity_detail'),


]
