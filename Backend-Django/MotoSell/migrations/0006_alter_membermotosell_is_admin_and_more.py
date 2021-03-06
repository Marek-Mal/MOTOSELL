# Generated by Django 4.0.2 on 2022-03-02 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0005_remove_membermotosell_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membermotosell',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='membermotosell',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='motosellmodel',
            name='displacement',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='motosellmodel',
            name='post_Moto',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='motosellmodel',
            name='power',
            field=models.PositiveBigIntegerField(),
        ),
    ]
