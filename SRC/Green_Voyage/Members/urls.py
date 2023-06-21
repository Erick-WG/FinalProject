from django.urls import path
#from . import views
from .views import  CreateUserView, LoginUser

urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register"),
    # create templates for these two below.
    path('admin/', LoginUser.as_view(), name = 'admin_dashboard'),
    path('Users/', LoginUser.as_view(), name = 'users_dashboard'),
]
