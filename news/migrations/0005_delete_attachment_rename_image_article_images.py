# Generated by Django 4.2 on 2023-06-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_attachment_rename_images_article_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='images',
        ),
    ]