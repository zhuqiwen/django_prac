# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 03:14
from __future__ import unicode_literals

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
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('comment', models.TextField()),
                ('is_suspended', models.BooleanField()),
                ('suspended_date', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='taste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taste', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('is_public', models.BooleanField(default=False)),
                ('file_path', models.FilePathField()),
                ('title', models.CharField(max_length=255)),
                ('duration', models.BigIntegerField()),
                ('instruction', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('view_count', models.IntegerField()),
                ('rating', models.SmallIntegerField()),
                ('is_suspended', models.BooleanField()),
                ('suspended_date', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='video_ingredient_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedme.ingredient')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedme.video')),
            ],
        ),
        migrations.CreateModel(
            name='video_tag_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedme.tag')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedme.video')),
            ],
        ),
        migrations.CreateModel(
            name='video_taste_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('taste_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedme.taste')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedme.video')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedme.video'),
        ),
    ]
