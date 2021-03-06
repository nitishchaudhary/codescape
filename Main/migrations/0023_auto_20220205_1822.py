# Generated by Django 3.1.1 on 2022-02-05 12:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0022_auto_20220205_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 12, 52, 36, 903963, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project_comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 12, 52, 36, 905962, tzinfo=utc)),
        ),
    ]
