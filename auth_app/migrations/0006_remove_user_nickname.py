# Generated by Django 5.0.4 on 2024-05-22 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]
