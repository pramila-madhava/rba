# Generated by Django 4.2.2 on 2023-07-14 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_collected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.CharField(default='Id not given', max_length=400)),
                ('userid', models.CharField(blank=True, default='something', max_length=400, null=True)),
                ('canvas', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('webgl', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, default=0, null=True)),
                ('longitude', models.FloatField(blank=True, default=0, null=True)),
                ('ip', models.CharField(blank=True, default='something', max_length=40, null=True)),
                ('time_zone', models.CharField(blank=True, default='UTC', max_length=40, null=True)),
                ('language', models.CharField(blank=True, default='en-US', max_length=40, null=True)),
                ('latlong', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('location', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('browser', models.TextField(blank=True, default='0', null=True)),
                ('Os', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('system_type', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('rtt', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('login_time', models.TimeField(default=0)),
                ('start_date', models.DateField(default=datetime.date.today, null=True)),
                ('screen_size', models.CharField(default=0, max_length=20)),
                ('start_week', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('login_status', models.CharField(blank=True, default='E', max_length=200, null=True)),
                ('login_count', models.IntegerField()),
                ('prev_date', models.DateField(default=datetime.date.today, null=True)),
                ('end_date', models.DateField(default=datetime.date.today, null=True)),
            ],
        ),
    ]
