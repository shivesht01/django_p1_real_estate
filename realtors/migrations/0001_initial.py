# Generated by Django 3.0.8 on 2020-08-16 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_mvp', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('email', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=20)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]