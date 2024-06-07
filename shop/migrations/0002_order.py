# Generated by Django 4.0 on 2024-06-07 20:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(blank='', default='', max_length=400)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('date', models.DateField(default=datetime.datetime(2024, 6, 7, 23, 52, 59, 399371))),
                ('states', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
