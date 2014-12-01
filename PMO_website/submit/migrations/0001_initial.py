# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import submit.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('sub_date', models.DateTimeField(default=datetime.date(2014, 11, 25), verbose_name='date published')),
                ('published', models.CharField(null=True, blank=True, max_length=255)),
                ('docfile', models.FileField(null=True, blank=True, upload_to=submit.models.file)),
                ('md5', models.CharField(null=True, blank=True, max_length=32)),
                ('summary', models.TextField(null=True, blank=True, max_length=500)),
                ('src_url', models.URLField(null=True, blank=True)),
                ('doc_url', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('partner_name', models.CharField(null=True, blank=True, max_length=200)),
                ('group', models.ForeignKey(to='submit.Groups')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
