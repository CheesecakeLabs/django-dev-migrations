# Generated by Django 2.2 on 2019-07-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_1', models.CharField(max_length=10)),
                ('field_2', models.IntegerField()),
            ],
        ),
    ]
