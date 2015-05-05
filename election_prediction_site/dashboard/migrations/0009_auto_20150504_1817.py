# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20150504_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(null=True),
        ),
    ]
