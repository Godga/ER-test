# Generated by Django 3.0.3 on 2020-02-16 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ER_test_app', '0006_auto_20200216_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberpacket',
            name='packet_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]