# Generated by Django 4.1.7 on 2023-03-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_customer_info_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_info',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
