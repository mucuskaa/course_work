from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, verbose_name='Ім\'я')
    nickname = models.CharField(max_length=50, blank=True, null=True, verbose_name='Нік')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Почта')
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата реєстрації')
    wallet = models.FloatField(default=0, validators=[MinValueValidator(0.00)], verbose_name='Баланс')

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name='Користувач'
        verbose_name_plural='Користувачі'
        ordering=['id', 'nickname', '-date_of_registration', 'username']