# Generated by Django 2.0 on 2020-03-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200302_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]