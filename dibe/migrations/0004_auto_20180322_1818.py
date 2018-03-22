# Generated by Django 2.0 on 2018-03-22 18:18

import dibe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dibe', '0003_auto_20180322_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[dibe.models.validate_min_length]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=300, validators=[dibe.models.validate_min_length]),
        ),
    ]