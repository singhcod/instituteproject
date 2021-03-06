# Generated by Django 3.0 on 2021-01-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('company', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('location', models.CharField(max_length=15)),
            ],
        ),
    ]
