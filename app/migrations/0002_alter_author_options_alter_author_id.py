# Generated by Django 4.1.7 on 2023-02-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
