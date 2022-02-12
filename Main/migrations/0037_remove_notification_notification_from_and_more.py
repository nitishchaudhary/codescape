# Generated by Django 4.0.2 on 2022-02-10 08:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0036_alter_notification_notification_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notification_from',
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 8, 1, 32, 214598, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 8, 1, 32, 215599, tzinfo=utc)),
        ),
    ]
