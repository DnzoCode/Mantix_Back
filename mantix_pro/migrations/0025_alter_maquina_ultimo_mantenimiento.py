# Generated by Django 4.2.6 on 2023-11-10 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0024_alter_maquina_maquina_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='ultimo_mantenimiento',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
