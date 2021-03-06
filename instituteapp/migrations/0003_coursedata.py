# Generated by Django 3.0 on 2021-01-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0002_contactdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.CharField(max_length=30)),
                ('start_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('duration', models.CharField(max_length=20)),
                ('trainer_name', models.CharField(max_length=20)),
                ('trainer_exep', models.IntegerField()),
            ],
        ),
    ]
