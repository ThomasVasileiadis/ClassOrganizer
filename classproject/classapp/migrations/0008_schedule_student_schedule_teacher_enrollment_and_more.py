# Generated by Django 5.0 on 2023-12-12 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0007_rename_teacher_id_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.student'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.teacher'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(through='classapp.Enrollment', to='classapp.course'),
        ),
    ]
