# Generated by Django 2.2.5 on 2020-12-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20201210_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='onehouseoneprice',
            name='house_ceng',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='楼层'),
        ),
    ]
