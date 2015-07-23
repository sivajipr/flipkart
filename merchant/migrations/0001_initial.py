# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('address3', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
