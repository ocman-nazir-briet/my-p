# Generated by Django 4.1.7 on 2023-02-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_author_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='testt',
            name='des',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
