# Generated by Django 2.2.5 on 2020-12-15 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0020_auto_20201209_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionfeedback',
            name='feedback_phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='联系方式'),
        ),
    ]
