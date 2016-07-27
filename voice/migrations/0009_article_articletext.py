# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0008_article_len_art'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articleText',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
