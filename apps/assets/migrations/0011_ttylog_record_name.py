# Generated by Django 2.1.3 on 2018-12-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_server_public_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttylog',
            name='record_name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='对象存储Name'),
        ),
    ]
