from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    wallet = models.FloatField(default=0, validators=[MinValueValidator(0.00)])

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username}"
