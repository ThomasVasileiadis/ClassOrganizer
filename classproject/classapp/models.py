from django.db import models
from datetime import datetime

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    english_level = models.CharField(max_length=50, default=' ')
    obligation_name = models.CharField(max_length=50, default=' ')
    obligation_datetime = models.DateTimeField(null=True, blank=True)
    monthly_pay = models.CharField(max_length=50, default=' ')
    courses = models.ManyToManyField('Course', through='Enrollment')
    
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    working_days = models.CharField(max_length=50, default='')
    courses = models.ManyToManyField('Course', related_name='teachers')

class Course(models.Model):
    course_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True) #primary key
    day = models.CharField(max_length=50) #day of the week
    start_time = models.CharField(max_length=50) #start time of the class
    end_time = models.CharField(max_length=50) #end time of the class
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

class Obligations(models.Model):
    obligation_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    due_date = models.DateField(default=datetime.now)
    due_time = models.TimeField(default=datetime.now)

class StudentCourse(models.Model):
    student_course_id = models.AutoField(primary_key=True) #primary key
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class StudentObligation(models.Model):
    student_obligation_id = models.AutoField(primary_key=True) #primary key
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    obligation_id = models.ForeignKey(Obligations, on_delete=models.CASCADE)

