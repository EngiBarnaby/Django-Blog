# Generated by Django 3.0.5 on 2020-06-16 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='profile2.png', null=True, upload_to='')),
                ('first_name', models.CharField(default='Информация отсутствует', max_length=200, null=True)),
                ('last_name', models.CharField(default='Информация отсутствует', max_length=200, null=True)),
                ('email', models.CharField(default='Информация отсутствует', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
