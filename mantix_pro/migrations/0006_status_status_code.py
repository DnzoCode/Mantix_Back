# Generated by Django 4.2.6 on 2023-10-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0005_events_ejecucion_events_tecnico'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='status_code',
            field=models.CharField(max_length=1, null=True),
        ),
    ]