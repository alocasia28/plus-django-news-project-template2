# Generated by Django 5.0 on 2023-12-10 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_category_newsstory_story_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsstory',
            old_name='story_image',
            new_name='story_image_URL',
        ),
    ]