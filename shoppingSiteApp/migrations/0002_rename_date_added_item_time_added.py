# Generated by Django 3.2.7 on 2022-04-24 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingSiteApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date_added',
            new_name='time_added',
        ),
    ]
