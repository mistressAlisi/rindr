# Generated by Django 3.2.8 on 2021-11-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_ticketmeantimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='difficulty',
            field=models.CharField(choices=[('1', '1  - Simplest'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 - Bloody hard.')], default='2', max_length=2, verbose_name='Ticket Debug Difficuly'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='system',
            field=models.CharField(choices=[('o', 'ODINs'), ('b', 'BlueJays'), ('m', 'Mattermost')], default='o', max_length=2, verbose_name='Ticket originated in System'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='team',
            field=models.TextField(default='N/A', max_length=200, verbose_name='Ticket for DT/Team'),
        ),
    ]
