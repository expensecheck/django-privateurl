# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 22:15
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.SlugField(max_length=40, validators=[django.core.validators.RegexValidator(b'^[-_a-zA-Z0-9]+$')], verbose_name='action')),
                ('token', models.SlugField(max_length=64, validators=[django.core.validators.RegexValidator(b'^[-a-zA-Z0-9]+$')], verbose_name='token')),
                ('expire', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='expire')),
                ('data', models.TextField(blank=True, verbose_name='data')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('hits_limit', models.PositiveIntegerField(default=1, help_text='Set 0 to unlimited.', verbose_name='hits limit')),
                ('hit_counter', models.PositiveIntegerField(default=0, verbose_name='hit counter')),
                ('first_hit', models.DateTimeField(blank=True, null=True, verbose_name='first hit')),
                ('last_hit', models.DateTimeField(blank=True, null=True, verbose_name='last hit')),
                ('auto_delete', models.BooleanField(default=False, help_text='Delete object if it can no longer be used.', verbose_name='auto delete')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('-created',),
                'db_table': 'privateurl_privateurl',
                'verbose_name': 'private url',
                'verbose_name_plural': 'private urls',
            },
        ),
        migrations.AlterUniqueTogether(
            name='privateurl',
            unique_together=set([('action', 'token')]),
        ),
    ]
