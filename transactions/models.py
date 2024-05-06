from django.core.validators import MinValueValidator
from django.db import models

TRANSACTION_TYPES = (
    ('income', 'income'),
    ('expenses', 'expenses'),
)


class Transaction(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(0.00)])
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth_app.User', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.amount}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.name
