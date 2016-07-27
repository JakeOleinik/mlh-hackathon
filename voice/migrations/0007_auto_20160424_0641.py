# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0006_keyword_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='articleText',
        ),
        migrations.RemoveField(
            model_name='article',
            name='built_dict',
        ),
        migrations.RemoveField(
            model_name='article',
            name='contentPackageID',
        ),
        migrations.RemoveField(
            model_name='article',
            name='publicationID',
        ),
        migrations.RemoveField(
            model_name='article',
            name='words_only',
        ),
    ]
