# Generated by Django 3.2.17 on 2023-05-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cunstruction', '0013_worker_probationperiod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='probationPeriod',
            new_name='probation_length',
        ),
        migrations.AddField(
            model_name='worker',
            name='probation_period',
            field=models.CharField(default=2, max_length=90),
            preserve_default=False,
        ),
    ]
