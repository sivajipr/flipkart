# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20150720_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'static/uploads/', blank=True),
        ),
    ]
