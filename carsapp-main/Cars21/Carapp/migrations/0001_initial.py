# Generated by Django 3.1 on 2023-08-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('ccompany', models.CharField(max_length=50)),
                ('cmodel', models.CharField(max_length=50)),
                ('cprice', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]