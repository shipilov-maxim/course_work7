# Generated by Django 4.2.11 on 2024-06-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='Время'),
        ),
    ]