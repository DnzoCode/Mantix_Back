# Generated by Django 4.2.6 on 2023-11-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0017_events_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='isClosed',
            field=models.CharField(default='N', max_length=1, null=True),
        ),
    ]
