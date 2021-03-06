# Generated by Django 3.1.1 on 2022-02-01 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0012_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='collabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collab_request', to='Main.project')),
                ('requesting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
