# Generated by Django 2.2.4 on 2019-08-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.TextField(blank=True, verbose_name='설명'),
        ),
    ]
