# Generated by Django 5.0.4 on 2024-05-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_category_type_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type_category',
            field=models.CharField(choices=[('income', 'income'), ('expense', 'expense')], default='income', max_length=40),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('income', 'income'), ('expense', 'expense')], max_length=50, verbose_name='Тип транзакції'),
        ),
    ]
