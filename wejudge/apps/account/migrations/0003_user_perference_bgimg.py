# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_perference_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='perference_bgimg',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]