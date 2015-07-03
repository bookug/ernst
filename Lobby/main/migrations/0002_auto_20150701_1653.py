# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='act',
            field=models.ForeignKey(default=0, to='main.Action'),
        ),
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(default=0, to='main.Room'),
        ),
    ]
