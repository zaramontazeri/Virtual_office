# Generated by Django 3.2 on 2022-03-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taketime', '0002_time_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='day',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
