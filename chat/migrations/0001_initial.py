# Generated by Django 4.2.16 on 2024-12-06 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0009_alter_video_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chat_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
