# Generated by Django 5.0 on 2023-12-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0011_alter_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
