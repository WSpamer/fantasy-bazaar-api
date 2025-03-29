# Generated by Django 5.1.7 on 2025-03-29 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('source', models.CharField(max_length=100)),
                ('is_homebrew', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('relationship', models.TextField()),
                ('unique_laws', models.TextField()),
                ('notes', models.TextField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.campaign')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.religion')),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.campaign')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.organizationtype')),
            ],
        ),
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.country')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('pointOfInterest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.pointofinterest')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.organization')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign_manager.town')),
            ],
        ),
    ]
