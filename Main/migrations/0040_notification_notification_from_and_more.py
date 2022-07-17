# Generated by Django 4.0.2 on 2022-02-10 08:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0039_alter_notification_notification_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_from',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 8, 15, 29, 651663, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 8, 15, 29, 653657, tzinfo=utc)),
        ),
    ]