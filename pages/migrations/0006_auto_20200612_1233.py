# Generated by Django 3.0.5 on 2020-06-12 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200612_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('publish',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьй'},
        ),
    ]
