""" This defines the model for our custom user definition

    This file defines a new custom user model (UserProfile) as well
    as a new object manager. UserProfile, defaults the username
    to mail by setting USER_NAME_FIELD='email'

    in the main project, settings.py, we set AUTH_USER_MODEL = "profile_api.UserProfile"
    which overrides the default authentication model.
    Django (most like - I haven't read the details here) uses the UserProfileManager
    bound to UserProfile.object in order to create the user record.

    see https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model
    for additional details.

"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
"""
https://docs.djangoproject.com/en/4.2/topics/db/models/
https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
https://docs.djangoproject.com/en/4.2/topics/auth/default/
https://github.com/jazzband/django-two-factor-auth
https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email
"""


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile

        :param email:
        :param name:
        :param password:
        :return:
        """
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)  # Standard procedure
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super use with given details"""
        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)  # Standard procedure
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()  # This instructs Django how to handle users
    USERNAME_FIELD = "email"  # This is required to for Django to use the email field as the user name
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve full name of user

        :return:
            name: A string representing the name
        """
        return self.name

    def get_short_name(self):
        """Retrieve short name of user

        :return:
            name: A string representing the name
        """
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return self.email
