# Generated by Django 3.0.5 on 2020-06-12 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mce',
            name='text2',
        ),
    ]