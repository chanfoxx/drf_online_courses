# Generated by Django 4.2.9 on 2024-01-06 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_courses', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время последнего обновления'),
        ),
    ]
