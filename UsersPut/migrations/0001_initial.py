# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concierto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=32)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('num_entradas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=128)),
                ('constitucion', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='concierto',
            name='grupo',
            field=models.ForeignKey(to='UsersPut.Grupo'),
        ),
    ]
