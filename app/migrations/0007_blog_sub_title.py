# Generated by Django 3.1.3 on 2021-05-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sub_title',
            field=models.CharField(default='', max_length=40),
        ),
    ]
