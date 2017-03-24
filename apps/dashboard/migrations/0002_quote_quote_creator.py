# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quote_creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.User'),
            preserve_default=False,
        ),
    ]