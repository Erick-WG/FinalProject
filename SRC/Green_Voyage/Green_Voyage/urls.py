from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    # creating our custom app urls.
    path('', include('Home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('Members.urls')),

    # built in urls.
    path("admin/",admin.site.urls),
]
