# Generated by Django 2.2.3 on 2019-07-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housekeep', '0003_auto_20190710_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_to_be_performed_by',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='next_occurring_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
