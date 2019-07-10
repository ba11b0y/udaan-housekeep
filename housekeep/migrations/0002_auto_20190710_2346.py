# Generated by Django 2.2.3 on 2019-07-10 18:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('housekeep', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_to_be_performed_by',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='asset',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='housekeep.Asset'),
        ),
        migrations.AlterField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='housekeep.Worker'),
        ),
    ]