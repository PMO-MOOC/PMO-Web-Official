# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0004_auto_20141124_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='sub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]
