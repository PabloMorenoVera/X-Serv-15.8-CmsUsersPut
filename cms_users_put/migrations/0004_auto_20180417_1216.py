# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_users_put', '0003_auto_20180416_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=128)),
                ('dir_acortada', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Viaje',
        ),
    ]
