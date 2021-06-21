# Generated by Django 3.2.4 on 2021-06-21 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyWorkShop', '0023_delete_footermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images', verbose_name='로고 이미지')),
                ('title', models.CharField(max_length=10, verbose_name='제목')),
                ('content', models.TextField(max_length=100, verbose_name='내용')),
            ],
            options={
                'verbose_name': '바닥 페이지',
            },
        ),
    ]