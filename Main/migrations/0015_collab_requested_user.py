# Generated by Django 3.1.1 on 2022-02-01 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0014_auto_20220201_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='collab',
            name='requested_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='requested_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
