# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matrix', models.CharField(default=b'000000000000000000000000000000000000000000000000000000000000000000000000000000000', max_length=81)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matrix', models.CharField(default=b'123456789234567891345678912456789123567891234678912345789123456891234567912345678', max_length=81)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='solutions',
            field=models.ManyToManyField(default=0, to='sudoku.Solution'),
        ),
    ]
