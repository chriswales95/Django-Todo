# Generated by Django 2.2.1 on 2019-05-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190508_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(verbose_name='date to be completed by'),
        ),
    ]