# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0003_auto_20141124_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='sub_date',
            field=models.DateField(blank=True, verbose_name='date published', null=True),
        ),
    ]
