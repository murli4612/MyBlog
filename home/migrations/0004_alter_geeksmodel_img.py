# Generated by Django 3.2.5 on 2021-07-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_geeksmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='img',
            field=models.ImageField(default='', upload_to='imgges/'),
        ),
    ]