# Generated by Django 3.2 on 2022-03-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role_manager', '0002_auto_20211106_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiurl',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='component',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='consumerproject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
