from django.shortcuts import render
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
        student_name = request.POST.get('name')
        student_lastname = request.POST.get('last_name')
        student_phone = request.POST.get('phone')
        student_level = request.POST.get('level')
        student_obligationname = request.POST.get('obligation_name')
        student_obligationdate = request.POST.get('obligation_datetime')

        if not student_obligationdate:
            student_obligationdate = None

        student = Student(name=student_name, last_name=student_lastname, phone=student_phone, english_level=student_level, obligation_name=student_obligationname, obligation_datetime=student_obligationdate)
        student.save()
        
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'student.html', context)

def student_info(request):   
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'studentinfo.html', context)
    
    


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

def teacher_info(request):
    data = Teacher.objects.all()
    context = {'data': data}
    return render(request, 'teacher_info.html', context)

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