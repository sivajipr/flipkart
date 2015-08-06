# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150728_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.IntegerField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(max_length=12),
        ),
    ]
