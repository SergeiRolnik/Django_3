# Generated by Django 4.0.4 on 2022-06-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(db_column='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(db_column='name_1', max_length=100),
        ),
    ]
