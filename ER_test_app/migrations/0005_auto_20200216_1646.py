# Generated by Django 3.0.3 on 2020-02-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ER_test_app', '0004_auto_20200216_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataaboutsending',
            old_name='number_set_id',
            new_name='packet_id',
        ),
    ]