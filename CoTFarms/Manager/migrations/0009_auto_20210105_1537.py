# Generated by Django 3.1.4 on 2021-01-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0008_auto_20210104_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowmilking',
            name='amount',
            field=models.FloatField(),
        ),
    ]
