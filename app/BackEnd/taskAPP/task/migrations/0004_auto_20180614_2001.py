# Generated by Django 2.0.6 on 2018-06-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20180614_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='concluded',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='edited',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='removed',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
