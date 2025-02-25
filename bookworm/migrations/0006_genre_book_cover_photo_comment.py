# Generated by Django 4.2.14 on 2024-08-10 09:17

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookworm', '0005_book_rating_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(help_text="Enter the books' genre.", max_length=100, verbose_name='genre')),
                ('sub_genre', models.TextField(help_text='Enter the sub-genre this book falls under.', verbose_name='sub-genre')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cover_photo',
            field=cloudinary.models.CloudinaryField(default='xx', max_length=255, verbose_name='image'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookworm.post')),
            ],
        ),
    ]
