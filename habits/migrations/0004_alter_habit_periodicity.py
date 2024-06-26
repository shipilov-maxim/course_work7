# Generated by Django 4.2.11 on 2024-05-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveIntegerField(choices=[(1, 'Каждый день'), (2, 'Каждый будний день'), (3, 'Каждые выходные'), (4, 'Каждую неделю')], default=1, verbose_name='Периодичность'),
        ),
    ]
