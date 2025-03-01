# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any extra fields you want, e.g. profile info
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username
