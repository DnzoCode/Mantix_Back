# Generated by Django 4.2.6 on 2023-11-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0021_alter_events_end_alter_events_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]
