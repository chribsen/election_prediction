# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20150503_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(max_length=191, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='from_id',
            field=models.CharField(default=None, max_length=191),
        ),
        migrations.AlterField(
            model_name='comment',
            name='from_name',
            field=models.CharField(default=None, max_length=191),
        ),
        migrations.AlterField(
            model_name='like',
            name='from_id',
            field=models.CharField(max_length=191),
        ),
        migrations.AlterField(
            model_name='like',
            name='from_name',
            field=models.CharField(max_length=191),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_id',
            field=models.CharField(max_length=191, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_name',
            field=models.CharField(max_length=191),
        ),
        migrations.AlterField(
            model_name='party',
            name='party_name',
            field=models.CharField(max_length=191),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=191, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='from_id',
            field=models.CharField(max_length=191),
        ),
        migrations.AlterField(
            model_name='reply',
            name='from_name',
            field=models.CharField(max_length=191),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_id',
            field=models.CharField(max_length=191, serialize=False, primary_key=True),
        ),
    ]
