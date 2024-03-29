# Generated by Django 4.2.6 on 2023-10-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0004_historial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayDate', models.DateTimeField(null=True)),
                ('isClosed', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
