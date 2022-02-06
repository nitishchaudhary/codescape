# Generated by Django 3.1.1 on 2022-02-05 13:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0024_auto_20220205_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 13, 25, 59, 706353, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 13, 25, 59, 708353, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Project_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='Main.project')),
            ],
        ),
    ]