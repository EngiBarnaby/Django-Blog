# Generated by Django 3.0.5 on 2020-06-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20200614_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/profile1.png', null=True, upload_to=''),
        ),
    ]
