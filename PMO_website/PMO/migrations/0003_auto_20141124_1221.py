# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PMO', '0002_home_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published', blank=True),
        ),
    ]
