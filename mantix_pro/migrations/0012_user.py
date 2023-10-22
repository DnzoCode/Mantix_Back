# Generated by Django 4.2.6 on 2023-10-22 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0011_events_maquina_alter_events_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('user_email', models.CharField(max_length=200, null=True, unique=True)),
                ('user_password', models.CharField(max_length=200, null=True)),
                ('user_token', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.role')),
                ('status', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.status')),
            ],
        ),
    ]
