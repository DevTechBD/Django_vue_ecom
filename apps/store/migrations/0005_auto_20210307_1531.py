# Generated by Django 3.1.7 on 2021-03-07 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210307_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qtys',
        ),
        migrations.DeleteModel(
            name='Qtys',
        ),
    ]
