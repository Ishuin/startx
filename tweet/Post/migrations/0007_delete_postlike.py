# Generated by Django 3.0.1 on 2020-01-04 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_auto_20200104_1245'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]
