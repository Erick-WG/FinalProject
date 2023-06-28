from django.contrib import admin
from .models import UserManager, BaseUserManager, AbstractBaseUser

admin.site.register('UserManager')
admin.site.register('BaseUserManager')
admin.site.register('AbstractBaseUser')