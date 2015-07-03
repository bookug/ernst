# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0002_auto_20150702_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
