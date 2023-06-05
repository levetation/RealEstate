# Generated by Django 4.1.4 on 2023-06-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_seller_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='seller_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='no name', max_length=250, unique=True, verbose_name='seller/company name or username'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('regular', 'Regular User'), ('seller', 'Seller User')], default='regular', max_length=10, verbose_name='user type'),
        ),
    ]
