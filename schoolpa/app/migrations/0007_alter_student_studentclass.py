# Generated by Django 4.1 on 2022-09-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_absent_attendance_pre_abs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentclass',
            field=models.TextField(blank=True, null=True),
        ),
    ]
