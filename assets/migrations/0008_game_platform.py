# Generated by Django 2.0.1 on 2018-02-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.Platform'),
        ),
    ]
