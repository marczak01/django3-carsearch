# Generated by Django 3.2.5 on 2022-01-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0009_alter_advert_year_of_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='year_of_production',
            field=models.DateTimeField(null=True),
        ),
    ]