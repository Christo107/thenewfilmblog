# Generated by Django 3.2.19 on 2023-06-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230620_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='bio',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='actor',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
