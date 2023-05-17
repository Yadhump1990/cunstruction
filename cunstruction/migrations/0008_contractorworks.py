# Generated by Django 3.2.17 on 2023-03-10 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cunstruction', '0007_auto_20230309_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='contractorWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.contractor')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.user')),
            ],
        ),
    ]