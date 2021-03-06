# Generated by Django 3.2.8 on 2021-10-30 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20211030_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='opened',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Ticket Initially Opened'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='responded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Ticket Initial Response'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Ticket Updated'),
        ),
    ]
