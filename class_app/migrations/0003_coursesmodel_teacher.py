# Generated by Django 5.0.6 on 2024-06-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0002_remove_studentclassmodel_courses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesmodel',
            name='teacher',
            field=models.CharField(default='Undefined', max_length=30),
        ),
    ]
