# Generated by Django 3.0.2 on 2020-05-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='slug', max_length=40, unique=True),
        ),
    ]