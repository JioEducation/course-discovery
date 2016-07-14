# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0005_auto_20160713_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='display_organization',
            field=models.CharField(null=True, max_length=255, blank=True, default=None),
        ),
        migrations.AddField(
            model_name='courserun',
            name='enable_jvc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courserun',
            name='room_key',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='display_organization',
            field=models.CharField(null=True, max_length=255, blank=True, default=None),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='enable_jvc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='room_key',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.TextField(null=True, blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='courserun',
            name='short_description_override',
            field=models.TextField(help_text="Short description specific for this run of a course. Leave this value blank to default to the parent course's short_description attribute.", null=True, blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='short_description',
            field=models.TextField(null=True, blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='historicalcourserun',
            name='short_description_override',
            field=models.TextField(help_text="Short description specific for this run of a course. Leave this value blank to default to the parent course's short_description attribute.", null=True, blank=True, default=None),
        ),
    ]
