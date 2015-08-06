# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20150720_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1000, null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(related_name=b'post_attach', blank=True, to='product.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
