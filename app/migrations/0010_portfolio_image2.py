# Generated by Django 3.1.3 on 2021-05-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210515_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image2',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]