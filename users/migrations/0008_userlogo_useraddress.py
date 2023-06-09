# Generated by Django 4.1.4 on 2023-06-06 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 2')),
                ('postcode', models.CharField(blank=True, max_length=12, null=True, verbose_name='Postcode')),
                ('city', models.CharField(blank=True, max_length=1024, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=1024, null=True, verbose_name='County')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
