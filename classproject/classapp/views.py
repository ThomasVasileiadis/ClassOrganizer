from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from django.views.generic.base import View
from .forms import StudentForm
from .models import Student


def home(request):
    return render(request, 'home.html')


def student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('name')
        student_lastname = request.POST.get('last_name')
        student_phone = request.POST.get('phone')
        student_level = request.POST.get('level')
        student_obligationname = request.POST.get('obligation_name')
        student_obligationdate = request.POST.get('obligation_datetime')
        monthly_pay = request.POST.get('monthly_pay')

        if not student_obligationdate:
            student_obligationdate = None

        student = Student(monthly_pay=monthly_pay, student_id=student_id, name=student_name, last_name=student_lastname, phone=student_phone, english_level=student_level, obligation_name=student_obligationname, obligation_datetime=student_obligationdate)
        student.save()
        
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'student.html', context)

def addstudent(request):
    if request.method == 'POST':
        student_name = request.POST.get('name')
        student_lastname = request.POST.get('last_name')
        student_phone = request.POST.get('phone')
        student_level = request.POST.get('level')
        student_obligationname = request.POST.get('obligation_name')
        student_obligationdate = request.POST.get('obligation_datetime')
        monthly_pay = request.POST.get('monthly_pay')

        if not student_obligationdate:
            student_obligationdate = None

        student = Student(monthly_pay=monthly_pay, name=student_name, last_name=student_lastname, phone=student_phone, english_level=student_level, obligation_name=student_obligationname, obligation_datetime=student_obligationdate)
        student.save()
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'addstudent.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm  # Import your StudentForm here

from django.shortcuts import render, get_object_or_404
from .models import Student
from .forms import StudentForm

def editstudent(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    print(f"Retrieved student: {student}")
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.last_name = form.cleaned_data['last_name']
            student.phone = form.cleaned_data['phone']
            student.english_level = form.cleaned_data['english_level']
            student.obligation_name = form.cleaned_data['obligation_name']
            student.obligation_datetime = form.cleaned_data['obligation_datetime']
            student.monthly_pay = form.cleaned_data['monthly_pay']

            if not student.obligation_datetime:
                student.obligation_datetime = None

            # Save the updated student object to the database
            student.save()
            print(f"Updated student: {student}")

            students = Student.objects.all()
            return render(request, 'student.html', {'student_id': student.student_id, 'data': students})
    else:
        form = StudentForm(instance=student)
    print(f"Form errors: {form.errors}")
    return render(request, 'editstudent.html', {'form': form, 'student': student})



def teacher(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('name')
        teacher_lastname = request.POST.get('last_name')
        teacher_phone = request.POST.get('phone')
        teacher_workingdays = request.POST.getlist('working_days')

        # Join the list into a string with a separator
        teacher_workingdays_str = ', '.join(teacher_workingdays)

        teacher = Teacher(name=teacher_name, last_name=teacher_lastname, phone=teacher_phone, working_days=teacher_workingdays_str)
        teacher.save()
    data = Teacher.objects.all()
    context = {'data': data}

    return render(request, 'teacher.html', context)

def addteacher(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('name')
        teacher_lastname = request.POST.get('last_name')
        teacher_phone = request.POST.get('phone')
        teacher_workingdays = request.POST.getlist('working_days')

        # Join the list into a string with a separator
        teacher_workingdays_str = ', '.join(teacher_workingdays)

        teacher = Teacher(name=teacher_name, last_name=teacher_lastname, phone=teacher_phone, working_days=teacher_workingdays_str)
        teacher.save()
    data = Teacher.objects.all()
    context = {'data': data}

    return render(request, 'addteacher.html', context)


def course(request):
    return render(request, 'course.html', {'course': course})


def schedule(request):
    return render(request, 'schedule.html', {'schedule': schedule})


def student_info(request):
    return render(request, 'student_info.html', {'student_info': student_info})

def teacher_info(request):
    return render(request, 'teacher_info.html', {'teacher_info': teacher_info})


def course_info(request):
    return render(request, 'course_info.html', {'course_info': course_info})