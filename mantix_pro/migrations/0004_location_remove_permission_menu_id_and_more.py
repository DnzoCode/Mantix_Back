# Generated by Django 4.2.6 on 2023-10-16 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantix_pro', '0003_menu_status_permission_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='permission',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='role_id',
        ),
        migrations.AddField(
            model_name='events',
            name='mensaje_reprogramado',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='turno',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ManyToManyField(to='mantix_pro.menu'),
        ),
        migrations.AddField(
            model_name='permission',
            name='role',
            field=models.ManyToManyField(to='mantix_pro.role'),
        ),
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.status'),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='has_permission',
            field=models.CharField(default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnico_name', models.CharField(max_length=200, null=True)),
                ('tecnico_apellido', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.status')),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquina_name', models.CharField(max_length=250, null=True)),
                ('maquina_modelo', models.CharField(max_length=250, null=True)),
                ('numero_serial', models.CharField(max_length=250, null=True)),
                ('ultimo_mantenimiento', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.location')),
                ('status', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.status')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='mantix_pro.status'),
        ),
    ]