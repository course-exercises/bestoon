# Generated by Django 4.1.7 on 2023-08-13 13:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kharj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tozihat', models.TextField()),
                ('tarikh', models.DateTimeField()),
                ('meghdar_kharj', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
