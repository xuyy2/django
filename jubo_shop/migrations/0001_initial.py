# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='商品名称', max_length=20)),
                ('number', models.IntegerField(verbose_name='数量')),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='Clerk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('join_time', models.DateTimeField(auto_now_add=True)),
                ('is_available', models.NullBooleanField()),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('serial_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('clerk', models.ForeignKey(to='jubo_shop.Clerk')),
            ],
            options={
                'verbose_name': '货柜',
                'verbose_name_plural': '货柜',
            },
        ),
        migrations.AddField(
            model_name='addgoods',
            name='clerk',
            field=models.ForeignKey(verbose_name='上货员', to='jubo_shop.Clerk'),
        ),
        migrations.AddField(
            model_name='addgoods',
            name='counter',
            field=models.ForeignKey(verbose_name='所属货柜', to='jubo_shop.Counter'),
        ),
    ]
