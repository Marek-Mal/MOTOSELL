# Generated by Django 4.0.2 on 2022-02-15 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberMotoSell',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(default='.', max_length=255)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': '_membermotosell',
            },
        ),
        migrations.CreateModel(
            name='MotoSellModel',
            fields=[
                ('Moto_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.PositiveBigIntegerField(default=100)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('motocykl', 'motocykl'), ('osobowy', 'osobowy'), ('ciężarowy', 'ciężarowy')], max_length=9)),
                ('mark', models.TextField()),
                ('model', models.TextField()),
                ('date_of_production', models.DateField()),
                ('course', models.PositiveBigIntegerField()),
                ('displacement', models.PositiveSmallIntegerField()),
                ('power', models.PositiveSmallIntegerField()),
                ('fuel', models.CharField(choices=[('benzyna', 'benzyna'), ('disel', 'disel'), ('LPG', 'LPG')], max_length=9)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('post_Moto', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
