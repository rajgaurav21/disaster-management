# Generated by Django 2.2.6 on 2019-10-13 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0007_merge_20191013_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='number',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
