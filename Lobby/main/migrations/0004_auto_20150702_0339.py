# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150702_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='act',
            field=models.ForeignKey(related_name='act_room', default=0, to='main.Action'),
        ),
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(related_name='room_user', default=0, to='main.Room'),
        ),
    ]
