# Generated by Django 2.0 on 2022-03-13 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220313_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='doc',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
