# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20170922_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='age',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='foot',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='taz',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='waist',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
