# Generated by Django 4.1 on 2023-04-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offhour',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Enter end date'),
        ),
        migrations.AddField(
            model_name='offhour',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Enter start date'),
        ),
        migrations.AlterField(
            model_name='offhour',
            name='end_time',
            field=models.TimeField(verbose_name='Enter end time'),
        ),
        migrations.AlterField(
            model_name='offhour',
            name='start_time',
            field=models.TimeField(verbose_name='Enter start time'),
        ),
    ]
