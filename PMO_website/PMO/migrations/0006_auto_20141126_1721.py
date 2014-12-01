# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PMO', '0005_auto_20141126_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('recent_upload', models.TextField(null=True, blank=True, max_length=500)),
                ('pub_date', models.DateTimeField(null=True, blank=True, verbose_name='date published')),
                ('user_name', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
