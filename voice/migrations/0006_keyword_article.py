# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0005_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='article',
            field=models.ForeignKey(default=None, to='voice.Article'),
            preserve_default=False,
        ),
    ]
