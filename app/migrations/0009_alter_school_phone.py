# Generated by Django 4.1.7 on 2023-02-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_school_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.IntegerField(),
        ),
    ]