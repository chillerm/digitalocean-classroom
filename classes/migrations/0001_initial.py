# Generated by Django 2.2.7 on 2019-12-17 01:16

import classes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('destroyed_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('droplet_count', models.IntegerField(default=1)),
                ('prefix', models.CharField(default=classes.models.prefix_generator, max_length=15)),
                ('droplet_image', models.CharField(max_length=50)),
                ('droplet_size', models.CharField(max_length=25)),
                ('droplet_region', models.CharField(max_length=50)),
                ('droplet_student_limit', models.IntegerField(default=1)),
                ('droplet_priv_net', models.BooleanField(default=False)),
                ('droplet_ipv6', models.BooleanField(default=False)),
                ('droplet_user_data', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
