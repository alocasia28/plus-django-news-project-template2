# Generated by Django 5.0 on 2023-12-10 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_story_image_newsstory_story_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='story_image_URL',
            field=models.URLField(default='No URL Defined'),
        ),
    ]