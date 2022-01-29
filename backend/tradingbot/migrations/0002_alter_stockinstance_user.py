# Generated by Django 3.2.8 on 2022-01-08 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tradingbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinstance',
            name='user',
            field=models.ForeignKey(help_text='Associated user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
