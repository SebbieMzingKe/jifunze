# Generated by Django 4.2.16 on 2024-12-03 05:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_course_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='file',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
