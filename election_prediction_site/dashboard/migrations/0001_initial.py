# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.CharField(max_length=400, serialize=False, primary_key=True)),
                ('comment', models.TextField()),
                ('like_count', models.IntegerField()),
                ('sentiment_score', models.FloatField()),
                ('is_negative', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page_id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('created_time', models.DateTimeField()),
                ('like_count', models.IntegerField()),
                ('share_count', models.IntegerField()),
                ('sentiment_score', models.FloatField()),
                ('is_negative', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.CharField(max_length=400, serialize=False, primary_key=True)),
                ('reply', models.TextField()),
                ('like_count', models.IntegerField()),
                ('sentiment_score', models.FloatField()),
                ('is_negative', models.BooleanField()),
                ('comment_id', models.ForeignKey(to='dashboard.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='page_id',
            field=models.ForeignKey(to='dashboard.Page'),
        ),
    ]
