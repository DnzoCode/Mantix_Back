# Generated by Django 4.2.6 on 2023-10-24 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0005_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='isClosed',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
