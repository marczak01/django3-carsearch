# Generated by Django 3.2.5 on 2022-01-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0016_auto_20220113_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='engine_capacity',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='mileage',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='num_of_doors',
            field=models.IntegerField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='power',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='year_of_production',
            field=models.IntegerField(max_length=4, null=True),
        ),
    ]
