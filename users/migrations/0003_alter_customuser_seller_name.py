# Generated by Django 4.1.4 on 2023-06-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_seller_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='seller_name',
            field=models.CharField(max_length=500, unique=True, verbose_name='Seller name'),
        ),
    ]
