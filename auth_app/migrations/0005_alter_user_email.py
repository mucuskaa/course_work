# Generated by Django 5.0.4 on 2024-05-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_user_options_alter_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Пошта'),
        ),
    ]
