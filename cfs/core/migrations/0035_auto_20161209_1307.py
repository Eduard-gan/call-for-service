# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20160630_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nature',
            options={'ordering': ('descr',)},
        ),
        migrations.AlterModelOptions(
            name='naturegroup',
            options={'ordering': ('descr',)},
        ),
    ]
