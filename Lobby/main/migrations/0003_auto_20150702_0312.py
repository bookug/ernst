# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150701_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomName',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='action',
            name='actName',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='action',
            name='actNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomSize',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickName',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
