# Generated by Django 2.0 on 2017-12-23 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dibe', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='host_ids',
        ),
        migrations.RemoveField(
            model_name='user',
            name='share_ids',
        ),
    ]
