from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default="1970-01-01")
    is_messadmin = models.BooleanField(default=False)
