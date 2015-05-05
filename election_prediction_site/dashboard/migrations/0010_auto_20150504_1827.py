# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20150504_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='share_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='like_count',
            field=models.IntegerField(null=True),
        ),
    ]
