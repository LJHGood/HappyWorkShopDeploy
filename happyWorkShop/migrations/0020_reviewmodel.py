# Generated by Django 3.2.4 on 2021-06-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyWorkShop', '0019_delete_reviewmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=10000)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
    ]
