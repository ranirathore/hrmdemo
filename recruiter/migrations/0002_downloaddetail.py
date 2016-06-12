# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downloaddetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=3)),
                ('total_downloads', models.IntegerField(max_length=2)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
