# Generated by Django 5.0 on 2023-12-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0009_teacher_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='working_hours',
            field=models.CharField(default='', max_length=50),
        ),
    ]
