# Generated by Django 4.0.3 on 2022-04-03 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
