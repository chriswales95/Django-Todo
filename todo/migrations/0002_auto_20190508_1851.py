# Generated by Django 2.2.1 on 2019-05-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(verbose_name='date to be done'),
        ),
    ]