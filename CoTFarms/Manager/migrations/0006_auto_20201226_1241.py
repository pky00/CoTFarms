# Generated by Django 3.1.4 on 2020-12-26 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0005_auto_20201225_1418'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Milking',
            new_name='CowMilking',
        ),
        migrations.RenameModel(
            old_name='MilkSale',
            new_name='CowMilkSale',
        ),
        migrations.RenameModel(
            old_name='Pregnancy',
            new_name='CowPregnancy',
        ),
    ]
