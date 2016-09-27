# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-09 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20160308_0847'),
        ('problem', '0002_tdmakerqueue'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemClassify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.User')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.ProblemClassify')),
            ],
        ),
        migrations.RemoveField(
            model_name='courseclassify',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseclassify',
            name='parent',
        ),
        migrations.AlterField(
            model_name='problem',
            name='classify',
            field=models.ManyToManyField(blank=True, to='problem.ProblemClassify'),
        ),
        migrations.DeleteModel(
            name='CourseClassify',
        ),
    ]