# Generated by Django 2.1a1 on 2018-06-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_productinorder_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
