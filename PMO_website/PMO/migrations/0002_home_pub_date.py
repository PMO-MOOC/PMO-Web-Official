# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PMO', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='pub_date',
            field=models.DateField(verbose_name='date published', null=True, blank=True),
            preserve_default=True,
        ),
    ]
