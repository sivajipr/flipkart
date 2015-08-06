# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='phone_number',
            new_name='pincode',
        ),
    ]
