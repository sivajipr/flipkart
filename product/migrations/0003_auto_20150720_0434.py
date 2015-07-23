# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20150717_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=20, choices=[(b'Electronics', b'Electronic products'), (b'Cloathing', b'Clothings'), (b'Mobiles', b'Mobile products'), (b'Books', b'Book products')]),
        ),
    ]
