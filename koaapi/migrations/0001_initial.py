# Generated by Django 4.2.1 on 2023-05-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('all_points', models.TextField(blank=True)),
                ('closest_points', models.TextField(blank=True)),
                ('coordinates', models.CharField(max_length=20)),
            ],
        ),
    ]