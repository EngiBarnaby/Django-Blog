# Generated by Django 3.0.5 on 2020-06-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200617_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
