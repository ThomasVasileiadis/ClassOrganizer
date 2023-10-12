from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True) #primary key
    day = models.CharField(max_length=50) #day of the week
    start_time = models.CharField(max_length=50) #start time of the class
    end_time = models.CharField(max_length=50) #end time of the class
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class Obligations(models.Model):
    obligation_id = models.AutoField(primary_key=True) #primary key
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    due_date = models.DateField()

class StudentCourse(models.Model):
    student_course_id = models.AutoField(primary_key=True) #primary key
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class StudentObligation(models.Model):
    student_obligation_id = models.AutoField(primary_key=True) #primary key
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    obligation_id = models.ForeignKey(Obligations, on_delete=models.CASCADE)