# Generated by Django 5.0 on 2023-12-06 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0006_student_monthly_pay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]