# Generated by Django 3.2.8 on 2021-10-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20211030_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='opened',
            field=models.DateTimeField(verbose_name='Ticket Initially Opened'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='responded',
            field=models.DateTimeField(verbose_name='Ticket Initial Response'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(verbose_name='Ticket Updated'),
        ),
    ]