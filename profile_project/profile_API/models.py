from django.db import models


## this two packages are needed 
## for overwriting the django default user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

## user profile models
## we overwrite the django default user models

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ database model for user in the system """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    ## this is the custom user manager
    ## so the django admin understand and interact how to deal with the new class
    ## specfy the model manager
    objects = UserProfileManager()

    ## we overwrite the default username field with emal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']



