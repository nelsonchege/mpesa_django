# Generated by Django 3.2.7 on 2021-09-09 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpesaApp', '0003_auto_20210909_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='Business_short_code',
            new_name='Business_short_code_db',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='company_phone_number',
            new_name='company_phone_number_db',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='amount',
            new_name='customer_amount',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='customer_phone_number',
            new_name='customer_phone_number_db',
        ),
    ]
