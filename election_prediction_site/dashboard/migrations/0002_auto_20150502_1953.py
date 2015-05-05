# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('party_name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.CharField(max_length=400, serialize=False, primary_key=True)),
                ('created_time', models.DateTimeField()),
                ('like_count', models.IntegerField()),
                ('share_count', models.IntegerField()),
                ('sentiment_score', models.FloatField()),
                ('is_negative', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='page',
            name='is_negative',
        ),
        migrations.RemoveField(
            model_name='page',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='page',
            name='sentiment_score',
        ),
        migrations.RemoveField(
            model_name='page',
            name='share_count',
        ),
        migrations.AddField(
            model_name='page',
            name='is_politician',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='page_name',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='page_id',
            field=models.ForeignKey(to='dashboard.Post'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_id',
            field=models.CharField(max_length=400, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='post',
            name='page_id',
            field=models.ForeignKey(to='dashboard.Page'),
        ),
        migrations.AddField(
            model_name='page',
            name='party',
            field=models.ForeignKey(default=None, to='dashboard.Party'),
            preserve_default=False,
        ),
    ]
