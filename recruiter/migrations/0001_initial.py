# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resume', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('work_experience', models.CharField(max_length=10)),
                ('analytics_exp', models.CharField(max_length=10)),
                ('current_location', models.CharField(max_length=10)),
                ('corrected_location', models.CharField(max_length=10)),
                ('nearest_city', models.CharField(max_length=10)),
                ('prefered_location', models.CharField(max_length=10)),
                ('ctc', models.CharField(max_length=10)),
                ('current_employer', models.CharField(max_length=20)),
                ('current_designation', models.CharField(max_length=30)),
                ('skill', models.CharField(max_length=50)),
                ('ug_cource', models.CharField(max_length=10)),
                ('ug_institute', models.CharField(max_length=20)),
                ('ug_passing_year', models.CharField(max_length=10)),
                ('pg_cource', models.CharField(max_length=10)),
                ('pg_institute', models.CharField(max_length=20)),
                ('trier1', models.CharField(max_length=10)),
                ('pg_passing_year', models.CharField(max_length=10)),
                ('post_pg_cource', models.CharField(max_length=10)),
                ('correct_post_pg', models.CharField(max_length=10)),
            ],
        ),
    ]
