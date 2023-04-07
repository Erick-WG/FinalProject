from typing import Required
from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, username, password, **extra_fields):
#         if not username:
#             raise ValueError('Email is required')
#         username = self.create_user(username)
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)
    
#     def _meta(self):
#         pass



# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=50)
#     password = models.CharField(max_length=23, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

# class Session(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=40, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)



