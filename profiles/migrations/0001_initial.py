# Generated by Django 4.2.14 on 2024-07-31 19:00

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('profile_picture', cloudinary.models.CloudinaryField(default=profiles.models.def_image, max_length=255, verbose_name='image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
