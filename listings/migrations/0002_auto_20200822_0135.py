# Generated by Django 3.0.8 on 2020-08-21 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='listings',
            new_name='Listing',
        ),
    ]
