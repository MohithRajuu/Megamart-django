# Generated by Django 3.1 on 2021-10-09 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20211010_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
