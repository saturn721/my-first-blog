# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import message.models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20170922_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='boobs',
            field=models.PositiveIntegerField(default=3, blank=True),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='eye_color',
            field=message.models.ColourField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='hair_color',
            field=message.models.ColourField(max_length=6, null=True, blank=True),
        ),
    ]
