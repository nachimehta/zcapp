# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nachi', '0002_auto_20150109_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table_number',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
    ]
