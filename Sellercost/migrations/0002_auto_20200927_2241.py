# Generated by Django 3.1 on 2020-09-27 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
        ('Usedproduct', '0001_initial'),
        ('Sellercost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellercost',
            name='employee_name',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.employee'),
        ),
        migrations.AddField(
            model_name='sellercost',
            name='usedproduct',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usedproduct.usedproduct'),
        ),
    ]
