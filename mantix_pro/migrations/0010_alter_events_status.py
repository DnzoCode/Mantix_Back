# Generated by Django 4.2.6 on 2023-10-22 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0009_alter_location_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.maquina'),
        ),
    ]
