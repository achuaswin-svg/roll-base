from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', _('User')),
        ('admin', _('Admin')),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
