# Generated by Django 2.0 on 2020-02-27 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image3',
        ),
    ]