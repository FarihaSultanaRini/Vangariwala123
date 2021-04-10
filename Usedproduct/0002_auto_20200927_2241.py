# Generated by Django 3.1 on 2020-09-27 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
        ('Buyer', '0001_initial'),
        ('Usedproduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedproduct',
            name='Buyer',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buyer.buyer'),
        ),
        migrations.AddField(
            model_name='usedproduct',
            name='seller',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.seller'),
        ),
    ]