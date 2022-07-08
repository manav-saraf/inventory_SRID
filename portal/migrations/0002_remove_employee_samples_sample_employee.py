# Generated by Django 4.0.5 on 2022-07-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='samples',
        ),
        migrations.AddField(
            model_name='sample',
            name='employee',
            field=models.ManyToManyField(related_name='samples', through='portal.Ownership', to='portal.employee'),
        ),
    ]
