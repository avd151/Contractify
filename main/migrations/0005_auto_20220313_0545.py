# Generated by Django 2.0 on 2022-03-13 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220313_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='budget',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
