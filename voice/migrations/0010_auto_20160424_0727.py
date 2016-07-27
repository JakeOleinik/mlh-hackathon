# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0009_article_articletext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='article',
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.RemoveField(
            model_name='article',
            name='len_art',
        ),
        migrations.AddField(
            model_name='article',
            name='built_dict',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='contentPackageID',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='publicationID',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='words_only',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
