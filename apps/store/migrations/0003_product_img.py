# Generated by Django 3.1.7 on 2021-03-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210305_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
