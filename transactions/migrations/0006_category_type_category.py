# Generated by Django 5.0.4 on 2024-05-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type_category',
            field=models.CharField(choices=[('income', 'income'), ('expenses', 'expenses')], default='income', max_length=40),
        ),
    ]
