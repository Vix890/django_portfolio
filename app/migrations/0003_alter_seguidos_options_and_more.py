# Generated by Django 5.0 on 2023-12-12 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_estudio_nota_media_notificacion_seguidor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seguidos',
            options={'ordering': ['seguido'], 'verbose_name': 'Seguidos', 'verbose_name_plural': 'Seguidos'},
        ),
        migrations.RenameField(
            model_name='seguidos',
            old_name='seguidos',
            new_name='seguido',
        ),
    ]
