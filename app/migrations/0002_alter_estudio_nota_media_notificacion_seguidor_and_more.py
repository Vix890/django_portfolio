# Generated by Django 5.0 on 2023-12-12 10:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudio',
            name='nota_media',
            field=models.CharField(max_length=255, verbose_name='Nota media'),
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrado', models.BooleanField(default=False)),
                ('notificacion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Notificacion')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creations', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notificacion',
                'verbose_name_plural': 'Notificaciones',
                'ordering': ['notificacion'],
            },
        ),
        migrations.CreateModel(
            name='Seguidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrado', models.BooleanField(default=False)),
                ('seguidor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seguidor')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creations', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Seguidor',
                'verbose_name_plural': 'Seguidores',
                'ordering': ['seguidor'],
            },
        ),
        migrations.CreateModel(
            name='Seguidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrado', models.BooleanField(default=False)),
                ('seguidos', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seguidos')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creations', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Seguidos',
                'verbose_name_plural': 'Seguidos',
                'ordering': ['seguidos'],
            },
        ),
    ]
