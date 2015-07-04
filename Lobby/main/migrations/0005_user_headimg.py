# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150702_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='headImg',
            field=models.FileField(default=0, upload_to=b'./upload/'),
        ),
    ]
