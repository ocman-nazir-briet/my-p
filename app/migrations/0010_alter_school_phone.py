# Generated by Django 4.1.7 on 2023-02-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_school_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(max_length=32),
        ),
    ]
