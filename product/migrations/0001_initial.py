# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0002_merchant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('selling_price', models.IntegerField(default=0)),
                ('original_price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('merchant', models.ForeignKey(to='merchant.Merchant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
