# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0003_question_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='matrix',
            field=models.CharField(default=b'123456789456789123789123456234567891567891234891234567345678912678912345912345678', max_length=81),
        ),
    ]
