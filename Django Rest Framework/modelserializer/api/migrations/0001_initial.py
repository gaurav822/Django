# Generated by Django 4.0.2 on 2022-02-28 13:47

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
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=40)),
                ('number', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
