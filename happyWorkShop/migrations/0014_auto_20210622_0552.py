# Generated by Django 3.2.4 on 2021-06-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyWorkShop', '0013_auto_20210622_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representativeintroductionmodel',
            name='content',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='자격 내용'),
        ),
        migrations.AlterField(
            model_name='representativeintroductionmodel',
            name='current_history',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='현재 이력'),
        ),
        migrations.AlterField(
            model_name='representativeintroductionmodel',
            name='past_history',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='과거 이력'),
        ),
        migrations.AlterField(
            model_name='representativeintroductionmodel',
            name='qualification',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='자격 내용'),
        ),
    ]
