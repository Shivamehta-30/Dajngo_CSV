# Generated by Django 3.2.6 on 2021-08-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_alter_customer_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='Username',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.AddField(
            model_name='customer',
            name='Phonenumber',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
