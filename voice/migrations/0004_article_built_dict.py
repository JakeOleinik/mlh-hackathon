# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0003_auto_20160423_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='built_dict',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
