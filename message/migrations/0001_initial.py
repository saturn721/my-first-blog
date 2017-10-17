# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('age', models.PositiveIntegerField(default=18)),
                ('eye_color', models.CharField(max_length=7, default='#000000')),
                ('rice', models.CharField(max_length=6)),
                ('boobs', models.PositiveIntegerField(default=3)),
                ('waist', models.PositiveIntegerField(default=40)),
                ('hair_color', models.CharField(max_length=7, default='#000000')),
                ('taz', models.PositiveIntegerField(default=60)),
                ('foot', models.PositiveIntegerField(default=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
