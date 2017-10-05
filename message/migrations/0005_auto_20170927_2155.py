# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import message.models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20170922_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='boobs',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='eye_color',
            field=message.models.ColourField(default=18, max_length=6),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='foot',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='hair_color',
            field=message.models.ColourField(default=18, max_length=6),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='taz',
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='waist',
            field=models.PositiveIntegerField(default=40),
        ),
    ]
