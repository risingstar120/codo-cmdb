# Generated by Django 2.1.3 on 2018-12-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0012_auto_20181213_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerAuthRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('user', models.CharField(max_length=32)),
                ('comment', models.CharField(blank=True, max_length=160, null=True)),
                ('server', models.ManyToManyField(blank=True, null=True, to='assets.Server')),
                ('servergroup', models.ManyToManyField(blank=True, null=True, to='assets.ServerGroup')),
            ],
            options={
                'verbose_name': '资产授权规则',
                'verbose_name_plural': '资产授权规则',
                'ordering': ['-id'],
            },
        ),
    ]
