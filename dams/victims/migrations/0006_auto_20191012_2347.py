# Generated by Django 2.2.5 on 2019-10-12 23:47

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('victims', '0005_auto_20191012_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victims',
            name='location',
            field=django_mysql.models.JSONField(default=None, null=True),
        ),
    ]