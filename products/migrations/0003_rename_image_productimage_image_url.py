# Generated by Django 5.1.1 on 2024-09-29 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_image_url_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='image_url',
        ),
    ]
