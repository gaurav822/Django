# Generated by Django 4.0.2 on 2022-02-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('pname', models.CharField(max_length=20)),
                ('pemail', models.CharField(max_length=30)),
                ('ppass', models.CharField(max_length=20)),
            ],
        ),
    ]