# Generated by Django 4.2.11 on 2024-04-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htapp2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=None),
        ),
    ]