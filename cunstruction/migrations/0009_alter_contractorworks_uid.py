# Generated by Django 3.2.17 on 2023-03-10 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cunstruction', '0008_contractorworks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractorworks',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cunstruction.user'),
        ),
    ]
