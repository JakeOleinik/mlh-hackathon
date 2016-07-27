# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publicationID', models.IntegerField(default=0, blank=True)),
                ('contentPackageID', models.IntegerField(default=0, blank=True)),
                ('articleID', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=128, blank=True)),
                ('title', models.CharField(max_length=128, blank=True)),
                ('author', models.CharField(max_length=128, blank=True)),
                ('Article Text', models.TextField(null=True, blank=True)),
                ('image', models.URLField(blank=True)),
                ('Introduction', models.TextField(blank=True)),
                ('publicationName', models.CharField(max_length=128, blank=True)),
                ('publicationDate', models.DateTimeField(blank=True)),
                ('Cleaned words', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
