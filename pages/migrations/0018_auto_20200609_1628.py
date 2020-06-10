# Generated by Django 3.0.5 on 2020-06-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20200609_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='pages.Tag'),
        ),
    ]
