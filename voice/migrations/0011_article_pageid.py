# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0010_auto_20160424_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pageID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
