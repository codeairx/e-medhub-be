# Generated by Django 3.1 on 2020-09-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('COD', 'CashOnDelivery')], default='COD', max_length=20),
        ),
    ]
