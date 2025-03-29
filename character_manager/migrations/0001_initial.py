# Generated by Django 5.1.7 on 2025-03-29 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('relationship_level', models.IntegerField()),
                ('notes', models.TextField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character_manager.category')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character_manager.occupation')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character_manager.race')),
            ],
        ),
    ]
