# Generated by Django 3.1 on 2020-10-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usedproduct', '0002_auto_20200927_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedproduct',
            name='product_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/product'),
        ),
    ]
