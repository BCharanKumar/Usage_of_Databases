# Generated by Django 5.0.7 on 2024-11-19 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=125)),
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('capital_id', models.IntegerField(primary_key=True, serialize=False)),
                ('capital_name', models.CharField(max_length=75)),
                ('cid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]