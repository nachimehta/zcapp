# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nachi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entree',
            name='menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='entrees',
            field=models.ManyToManyField(to='nachi.Entree'),
            preserve_default=True,
        ),
    ]
