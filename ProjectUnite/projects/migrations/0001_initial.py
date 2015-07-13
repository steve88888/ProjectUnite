# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTitle',
            fields=[
                ('project', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('team_members', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
