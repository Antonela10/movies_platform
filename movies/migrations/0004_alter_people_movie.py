# Generated by Django 4.2.4 on 2023-08-31 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_photo_file_name_people_person_photo_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='movie',
            field=models.ManyToManyField(blank=True, related_name='movie', to='movies.movies'),
        ),
    ]
