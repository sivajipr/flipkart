# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150729_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
