# Generated by Django 5.0.1 on 2024-04-20 02:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=65)),
                ('descreption', models.CharField(max_length=165)),
                ('slug', models.SlugField()),
                ('preparation_time_unit', models.CharField(max_length=65)),
                ('servigs_unit', models.CharField(max_length=65)),
                ('preparatio_steps', models.TextField()),
                ('preparatio_steps_is_html', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_publeshed', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
