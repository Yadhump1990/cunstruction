# Generated by Django 3.2.17 on 2023-05-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cunstruction', '0014_auto_20230505_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=90, unique=True),
        ),
    ]
