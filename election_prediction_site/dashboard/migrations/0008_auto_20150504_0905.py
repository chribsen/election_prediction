# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20150504_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_clean',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_clean',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
