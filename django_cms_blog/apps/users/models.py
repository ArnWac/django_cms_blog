from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):

    email = models.EmailField(
        _('email address'),
        unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()