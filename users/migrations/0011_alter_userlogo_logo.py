# Generated by Django 4.1.4 on 2023-06-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_userlogo_photo_userlogo_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/users', verbose_name='logo'),
        ),
    ]