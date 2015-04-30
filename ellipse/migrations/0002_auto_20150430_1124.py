# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ellipse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='task',
        ),
        migrations.AddField(
            model_name='useractivity',
            name='obj',
            field=models.CharField(default=b'unknown', max_length=100),
        ),
    ]
