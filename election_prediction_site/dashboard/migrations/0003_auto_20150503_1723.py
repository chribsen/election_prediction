# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150502_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='page_id',
            new_name='post_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_count',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='from_id',
            field=models.CharField(default=None, max_length=400),
        ),
        migrations.AddField(
            model_name='comment',
            name='from_name',
            field=models.CharField(default=None, max_length=400),
        ),
        migrations.AddField(
            model_name='like',
            name='from_id',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='from_name',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='created_time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='from_id',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='from_name',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
    ]
