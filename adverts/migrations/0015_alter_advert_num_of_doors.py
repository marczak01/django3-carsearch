# Generated by Django 3.2.5 on 2022-01-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0014_alter_advert_num_of_doors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='num_of_doors',
            field=models.IntegerField(null=True),
        ),
    ]