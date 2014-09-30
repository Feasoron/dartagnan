# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('streetAddress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipCode', models.CharField(max_length=10)),
                ('monday_opens_at', models.TimeField(null=True, blank=True)),
                ('monday_closes_at', models.TimeField(null=True, blank=True)),
                ('tuesday_opens_at', models.TimeField(null=True, blank=True)),
                ('tuesday_closes_at', models.TimeField(null=True, blank=True)),
                ('wednesday_opens_at', models.TimeField(null=True, blank=True)),
                ('wednesday_closes_at', models.TimeField(null=True, blank=True)),
                ('thursday_opens_at', models.TimeField(null=True, blank=True)),
                ('thursday_closes_at', models.TimeField(null=True, blank=True)),
                ('friday_opens_at', models.TimeField(null=True, blank=True)),
                ('friday_closes_at', models.TimeField(null=True, blank=True)),
                ('saturday_opens_at', models.TimeField(null=True, blank=True)),
                ('saturday_closes_at', models.TimeField(null=True, blank=True)),
                ('sunday_opens_at', models.TimeField(null=True, blank=True)),
                ('sunday_closes_at', models.TimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isOnSale', models.BooleanField(default=False)),
                ('salePrice', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('category', models.ForeignKey(to='menu.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RestaurantInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('aboutUs', models.TextField(max_length=10000)),
                ('introBlurb', models.TextField(max_length=2000)),
                ('founded', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
