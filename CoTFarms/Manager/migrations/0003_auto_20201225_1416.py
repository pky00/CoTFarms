# Generated by Django 3.1.4 on 2020-12-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_auto_20201222_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cow',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cow',
            name='isMilking',
            field=models.BooleanField(default=False),
        ),
    ]
