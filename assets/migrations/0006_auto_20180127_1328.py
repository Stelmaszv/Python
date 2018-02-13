# Generated by Django 2.0.1 on 2018-01-27 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20180127_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mygames',
            name='game',
        ),
        migrations.RemoveField(
            model_name='mygames',
            name='user',
        ),
        migrations.AlterField(
            model_name='mylibrary',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='MyGames',
        ),
    ]
