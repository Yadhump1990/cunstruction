# Generated by Django 3.2.17 on 2023-03-08 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cunstruction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='job',
            name='wid',
        ),
    ]
