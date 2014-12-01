# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='sub_date',
            field=models.DateField(verbose_name='date published', blank=True, null=True),
        ),
    ]
