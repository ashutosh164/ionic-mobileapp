# Generated by Django 4.2 on 2023-04-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profiles_joined_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='image',
            field=models.ImageField(default='download.png', upload_to='profile'),
        ),
    ]