# Generated by Django 3.1.1 on 2020-10-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usedproduct', '0003_usedproduct_product_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedproduct',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
