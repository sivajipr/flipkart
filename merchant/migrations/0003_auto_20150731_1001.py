# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0002_merchant_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='phone_number',
            field=models.CharField(default=0, max_length=12),
        ),
    ]
