# Generated by Django 3.2.4 on 2021-06-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyWorkShop', '0020_reviewmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionModel',
        ),
        migrations.AlterModelOptions(
            name='contactusmodel',
            options={'verbose_name': '문의내용'},
        ),
        migrations.AlterModelOptions(
            name='introducemodel',
            options={'verbose_name': '소개 페이지'},
        ),
        migrations.AlterModelOptions(
            name='representativeintroductionmodel',
            options={'verbose_name': '대표소개 페이지'},
        ),
        migrations.AlterModelOptions(
            name='reviewmodel',
            options={'verbose_name': '후기 페이지'},
        ),
        migrations.AlterModelOptions(
            name='servicemodel',
            options={'verbose_name': '서비스 페이지'},
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='content',
            field=models.TextField(max_length=10000, verbose_name='후기 내용'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='후기 사진'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='name',
            field=models.CharField(max_length=200, verbose_name='후기 이름'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='title',
            field=models.CharField(max_length=500, verbose_name='후기 제목'),
        ),
    ]