# Generated by Django 4.1.4 on 2023-02-10 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.TextField(max_length=2000),
        ),
    ]
