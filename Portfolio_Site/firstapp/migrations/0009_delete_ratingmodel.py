# Generated by Django 5.0 on 2024-01-20 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_alter_ratingmodel_project_ratingmodel_average_rating_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RatingModel',
        ),
    ]
