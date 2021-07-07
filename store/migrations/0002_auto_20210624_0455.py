# Generated by Django 3.2.4 on 2021-06-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selleritem',
            name='product_category',
        ),
        migrations.AddField(
            model_name='selleritem',
            name='product_category',
            field=models.ManyToManyField(blank=True, null=True, to='store.Category'),
        ),
    ]