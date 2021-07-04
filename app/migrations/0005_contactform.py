# Generated by Django 3.1.3 on 2021-05-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_blog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(max_length=20)),
                ('yourEmail', models.CharField(max_length=40)),
                ('yourSubject', models.CharField(max_length=20)),
                ('ourMessage', models.TextField()),
            ],
        ),
    ]