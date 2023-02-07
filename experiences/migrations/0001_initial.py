# Generated by Django 4.1.4 on 2023-02-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=250)),
                ('country', models.CharField(default='S.Korea', max_length=50)),
                ('city', models.CharField(default='Seoul', max_length=80)),
                ('price', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=250)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=250)),
                ('explanation', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]