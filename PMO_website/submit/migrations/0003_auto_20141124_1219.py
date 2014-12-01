# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0002_auto_20141124_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='sub_date',
            field=models.DateTimeField(null=True, verbose_name='date published', blank=True),
        ),
    ]
