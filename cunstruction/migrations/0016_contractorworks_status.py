# Generated by Django 3.2.17 on 2023-05-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cunstruction', '0015_alter_login_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractorworks',
            name='status',
            field=models.CharField(default=2, max_length=90),
            preserve_default=False,
        ),
    ]
