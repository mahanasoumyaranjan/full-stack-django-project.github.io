
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
# Create your models here.

# class account(AbstractBaseUser):
#     userName = models.CharField(max_length=50 , unique=True)
#     password = models.CharField(max_length=20)
#     last_login = models.DateTimeField(verbose_name='last_login' , auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)


class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100 )
    userName = models.CharField(max_length=50 , unique=True)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    address = models.TextField()
    password = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    logged_in = models.BooleanField(default=False)
    def __str__(self):
        return self.firstName
