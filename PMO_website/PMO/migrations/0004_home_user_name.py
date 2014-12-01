# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PMO', '0003_auto_20141124_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='user_name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
