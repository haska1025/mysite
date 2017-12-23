# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-22 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IOStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.IntegerField()),
                ('recvbytes', models.IntegerField()),
                ('sendbytes', models.IntegerField()),
                ('recvpkgs', models.IntegerField()),
                ('sendpkgs', models.IntegerField()),
                ('clearpkgs', models.IntegerField()),
                ('cachepkgs', models.IntegerField()),
                ('clearbytes', models.IntegerField()),
                ('cachebytes', models.IntegerField()),
                ('recvlosts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confid', models.IntegerField()),
                ('uid', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='iostat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.User'),
        ),
    ]