# Generated by Django 4.1.7 on 2023-07-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Imagen'),
        ),
    ]
