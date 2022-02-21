# Generated by Django 4.0.2 on 2022-02-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='账号')),
                ('auth_key', models.CharField(max_length=100, verbose_name='口令')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
                'db_table': 'app_user',
            },
        ),
    ]
