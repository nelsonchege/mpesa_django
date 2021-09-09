# Generated by Django 3.2.7 on 2021-09-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesaApp', '0002_auto_20210908_0302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='first_name',
            new_name='Business_short_code',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='last_name',
            new_name='company_phone_number',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='middle_name',
            new_name='customer_phone_number',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='description',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='reference',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
