# Generated by Django 5.0.6 on 2024-07-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
