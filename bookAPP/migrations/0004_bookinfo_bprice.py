# Generated by Django 2.2.7 on 2019-11-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookAPP', '0003_auto_20191123_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bprice',
            field=models.DecimalField(decimal_places=2, default=16.99, max_digits=6),
        ),
    ]
