# Generated by Django 2.0.5 on 2021-07-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0006_auto_20210722_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]