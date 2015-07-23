# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20150720_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(default=0),
        ),
    ]
