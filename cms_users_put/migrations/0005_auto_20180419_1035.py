# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_users_put', '0004_auto_20180417_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='dir_acortada',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='page',
            name='direccion',
        ),
        migrations.AddField(
            model_name='page',
            name='pagina',
            field=models.TextField(null=True, blank=True),
        ),
    ]
