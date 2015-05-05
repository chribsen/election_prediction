# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20150503_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(default=None, to='dashboard.Post'),
            preserve_default=False,
        ),
    ]
