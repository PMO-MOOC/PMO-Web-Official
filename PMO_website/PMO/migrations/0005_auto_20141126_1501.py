# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('PMO', '0004_home_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='recent_upload',
            field=tinymce.models.HTMLField(max_length=500, blank=True, null=True),
        ),
    ]
