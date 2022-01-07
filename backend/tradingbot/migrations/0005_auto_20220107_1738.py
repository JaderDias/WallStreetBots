# Generated by Django 3.2.8 on 2022-01-07 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tradingbot', '0004_order_portfolio_stockinstance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['user', 'timestamp', 'order_type']},
        ),
        migrations.RemoveField(
            model_name='order',
            name='company',
        ),
        migrations.AddField(
            model_name='order',
            name='stock',
            field=models.ForeignKey(default=1, help_text='associated stock', on_delete=django.db.models.deletion.CASCADE, to='tradingbot.stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_type',
            field=models.CharField(choices=[('B', 'Buy'), ('S', 'Sell')], default='B', help_text='buy or sell transaction type', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('M', 'Market'), ('L', 'Limit'), ('S', 'Stop'), ('ST', 'Stop Limit'), ('T', 'Trailing Stop')], help_text='order type', max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='order price', max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(help_text='associated user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
