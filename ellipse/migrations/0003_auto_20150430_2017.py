# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ellipse', '0002_auto_20150430_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='added_on',
            field=models.DateField(default=b'30 Apr, 2015'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=b'30 Apr, 2015'),
        ),
    ]
