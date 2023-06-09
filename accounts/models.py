from django.db import models
import os
from django.contrib import auth
from django.urls import reverse
from django.db.models.signals import post_save

# for custom user
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''Model representation for user'''
    username = models.CharField(max_length=50, verbose_name="Your username ", unique=True)
    fname = models.CharField(max_length=50, verbose_name="First Name")
    lname = models.CharField(max_length=50, verbose_name="Last Name", default=None)
    email = models.EmailField(max_length=50, unique=True, blank=False, verbose_name="Your Email ")
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, verbose_name="Your profile picture ", null=True, default=None)
    is_active = models.BooleanField(default=True) # anyone who signs up for thsi application is by default an active user   
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) # the person who has highest level of control over database

    # need to specify manager class for this user
    objects = CustomUserManager()

    # we are not placing password field here because the password field will always be required
    REQUIRED_FIELDS = ['fname','lname','email', 'profile_pic']

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def fullname(self):
        return self.fname +" " + self.lname
    
    def get_absolute_url(self):
        return reverse("accounts:account_details", kwargs={"pk": self.pk})

    