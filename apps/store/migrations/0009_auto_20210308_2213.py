# Generated by Django 3.1.7 on 2021-03-08 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='store.product'),
        ),
    ]
