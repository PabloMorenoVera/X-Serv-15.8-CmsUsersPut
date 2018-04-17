# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_users_put', '0002_auto_20180416_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='viaje',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
