# Generated by Django 3.2.3 on 2021-05-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20210520_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='qty',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
