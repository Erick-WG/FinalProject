from django.contrib import admin
from .models import  User, UserManager, Session


admin.site.register(UserManager())
admin.site.register(Session())
admin.site.register(User())


