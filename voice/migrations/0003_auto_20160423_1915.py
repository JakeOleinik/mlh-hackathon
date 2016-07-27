# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0002_auto_20160423_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Article Text',
            new_name='articleText',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Introduction',
            new_name='introduction',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Cleaned words',
            new_name='words_only',
        ),
    ]
