# Generated by Django 3.0.5 on 2020-05-28 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200528_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecontent',
            name='article',
        ),
    ]