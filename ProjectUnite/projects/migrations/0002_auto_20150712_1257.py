# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecttitle',
            old_name='project',
            new_name='projectID',
        ),
    ]
