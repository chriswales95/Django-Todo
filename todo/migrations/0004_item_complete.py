# Generated by Django 2.2.1 on 2019-05-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20190508_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
