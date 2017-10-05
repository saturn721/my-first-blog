# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import message.models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordering',
            old_name='text',
            new_name='message',
        ),
        migrations.AddField(
            model_name='ordering',
            name='age',
            field=models.PositiveIntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordering',
            name='boobs',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordering',
            name='eye_color',
            field=message.models.ColourField(default=12, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordering',
            name='foot',
            field=models.PositiveIntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordering',
            name='hair_color',
            field=message.models.ColourField(default=12, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordering',
            name='rice',
            field=models.CharField(default='Asia', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordering',
            name='taz',
            field=models.PositiveIntegerField(default=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordering',
            name='waist',
            field=models.PositiveIntegerField(default=30),
            preserve_default=False,
        ),
    ]
