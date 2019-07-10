# Generated by Django 2.2.3 on 2019-07-10 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housekeep', '0002_auto_20190710_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='asset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='housekeep.Asset'),
        ),
        migrations.AlterField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='housekeep.Worker'),
        ),
    ]