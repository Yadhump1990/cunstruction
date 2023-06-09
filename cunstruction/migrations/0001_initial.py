# Generated by Django 3.2.17 on 2023-03-06 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=90)),
                ('lname', models.CharField(max_length=90)),
                ('gender', models.CharField(max_length=90)),
                ('phone', models.BigIntegerField()),
                ('place', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=90)),
                ('pin', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=200)),
                ('jobStatus', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.contractor')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=90)),
                ('lname', models.CharField(max_length=90)),
                ('gender', models.CharField(max_length=90)),
                ('phone', models.BigIntegerField()),
                ('place', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=90)),
                ('pin', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.login')),
            ],
        ),
        migrations.CreateModel(
            name='worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=90)),
                ('lname', models.CharField(max_length=90)),
                ('gender', models.CharField(max_length=90)),
                ('phone', models.BigIntegerField()),
                ('place', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=90)),
                ('pin', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.IntegerField()),
                ('availability', models.CharField(max_length=90)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.contractor')),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.login')),
            ],
        ),
        migrations.CreateModel(
            name='wkr_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('rating', models.IntegerField()),
                ('date', models.DateField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.contractor')),
                ('wid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.worker')),
            ],
        ),
        migrations.CreateModel(
            name='wkr_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.contractor')),
                ('wid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.worker')),
            ],
        ),
        migrations.CreateModel(
            name='usr_work_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.contractor')),
                ('jid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.job')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.user')),
            ],
        ),
        migrations.CreateModel(
            name='usr_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('rating', models.IntegerField()),
                ('date', models.DateField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.user')),
            ],
        ),
        migrations.CreateModel(
            name='usr_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.user')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.user'),
        ),
        migrations.AddField(
            model_name='job',
            name='wid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.worker'),
        ),
        migrations.AddField(
            model_name='contractor',
            name='lid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cunstruction.login'),
        ),
    ]
