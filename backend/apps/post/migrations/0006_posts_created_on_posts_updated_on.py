# Generated by Django 4.2 on 2023-04-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_posts_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
