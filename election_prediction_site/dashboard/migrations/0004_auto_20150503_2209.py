# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20150503_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_negative',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='sentiment_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_negative',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='sentiment_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='is_negative',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='sentiment_score',
            field=models.FloatField(null=True),
        ),
    ]
