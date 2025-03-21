# Generated by Django 3.2.25 on 2025-03-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image_width',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='is_color',
            field=models.BooleanField(null=True),
        ),
    ]
