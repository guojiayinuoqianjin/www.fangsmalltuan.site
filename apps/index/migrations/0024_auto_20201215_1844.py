# Generated by Django 2.2.5 on 2020-12-15 18:44

from django.db import migrations, models
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0023_onehouseoneprice_house_ceng'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='building_fk',
        ),
        migrations.RemoveField(
            model_name='share',
            name='classfiy',
        ),
        migrations.AddField(
            model_name='share',
            name='bd_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='顾问主营楼盘id'),
        ),
        migrations.AddField(
            model_name='share',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='share',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='share',
            name='head_img',
            field=utils.fields.QiniuField(blank=True, max_length=500, null=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='share',
            name='img',
            field=utils.fields.QiniuField(blank=True, max_length=500, null=True, verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='share',
            name='video',
            field=utils.fields.QiniuField(blank=True, max_length=500, null=True, verbose_name='视频'),
        ),
    ]