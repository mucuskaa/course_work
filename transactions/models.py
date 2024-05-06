from django.core.validators import MinValueValidator
from django.db import models

TRANSACTION_TYPES = (
    ('income', 'income'),
    ('expenses', 'expenses'),
)


class Transaction(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(0.00)], verbose_name='Сума')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    user = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, verbose_name='Користувач')
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES, verbose_name='Тип транзакції')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категорія')

    def __str__(self):
        return f"{self.amount}"

    class Meta:
        verbose_name = 'Транзакція'
        verbose_name_plural = 'транзакції'
        ordering = ['id', '-date', 'user', 'transaction_type', 'category']


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категорія')
    image = models.ImageField(upload_to='category_images', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id', 'name']