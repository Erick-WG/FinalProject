from django.contrib import admin
from .models import user, UserManager, Session

admin.site.register(user())
admin.site.register(UserManager())
admin.site.register(Session())

