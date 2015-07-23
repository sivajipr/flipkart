# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
