# Generated by Django 4.2.6 on 2023-10-27 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0010_alter_user_managers_user_last_login_user_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]