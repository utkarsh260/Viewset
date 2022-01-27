# Generated by Django 3.2.10 on 2022-01-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=200, null=True, unique=True, verbose_name='emailaddress')),
                ('mobile_no', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
