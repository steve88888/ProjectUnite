# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150712_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttitle',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
