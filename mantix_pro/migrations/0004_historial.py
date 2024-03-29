# Generated by Django 4.2.6 on 2023-10-23 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0003_alter_events_maquina_alter_events_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_change', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.events')),
                ('status', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.user')),
            ],
        ),
    ]
