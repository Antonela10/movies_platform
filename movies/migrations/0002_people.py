# Generated by Django 4.2.4 on 2023-08-31 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('photo_file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('character_name', models.CharField(blank=True, max_length=255, null=True)),
                ('stroer_id', models.IntegerField(blank=True, null=True)),
                ('movie', models.ManyToManyField(blank=True, null=True, related_name='movie', to='movies.movies')),
            ],
        ),
    ]
