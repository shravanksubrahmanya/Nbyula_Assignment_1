# Generated by Django 4.1 on 2023-04-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_scheduler', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Enter the title of the meeting'),
        ),
    ]
