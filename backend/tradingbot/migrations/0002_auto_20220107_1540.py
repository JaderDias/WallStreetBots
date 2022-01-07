# Generated by Django 3.2.8 on 2022-01-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='news',
            field=models.ManyToManyField(blank=True, to='tradingbot.News'),
        ),
        migrations.AlterField(
            model_name='company',
            name='tweets',
            field=models.ManyToManyField(blank=True, to='tradingbot.Tweets'),
        ),
    ]
