# Generated by Django 2.0.1 on 2018-02-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0012_auto_20180226_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylibrary',
            name='games',
            field=models.ManyToManyField(related_name='Game', related_query_name='Game', to='assets.Game'),
        ),
    ]
