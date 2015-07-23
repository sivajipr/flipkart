# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'/static/uploads/', blank=True),
        ),
    ]
