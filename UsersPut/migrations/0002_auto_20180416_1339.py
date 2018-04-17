# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersPut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('nif', models.CharField(max_length=32)),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('destino', models.CharField(max_length=32)),
                ('locomocion', models.CharField(max_length=32)),
                ('alojamiento', models.CharField(max_length=32)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='concierto',
            name='grupo',
        ),
        migrations.DeleteModel(
            name='Concierto',
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='viaje',
            field=models.ForeignKey(to='UsersPut.Viaje'),
        ),
    ]
