# Generated by Django 2.2.5 on 2020-12-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0009_auto_20201201_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersealstatus',
            name='statue',
            field=models.BooleanField(default=False, verbose_name='是否封号'),
        ),
    ]
