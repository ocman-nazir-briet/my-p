# Generated by Django 4.1.7 on 2023-02-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_school_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(help_text='must contain 11 digits', max_length=32),
        ),
    ]