# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_buy_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
