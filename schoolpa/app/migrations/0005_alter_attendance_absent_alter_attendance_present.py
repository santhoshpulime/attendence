# Generated by Django 4.1 on 2022-09-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='absent',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='present',
            field=models.TextField(blank=True),
        ),
    ]
