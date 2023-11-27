from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render


class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    
class TeacherView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CourseView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ScheduleView(APIView):
    def get(self, request):
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ObligationsView(APIView):
    def get(self, request):
        obligations = Obligations.objects.all()
        serializer = ObligationsSerializer(obligations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ObligationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class StudentCourseView(APIView):
    def get(self, request):
        student_courses = StudentCourse.objects.all()
        serializer = StudentCourseSerializer(student_courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class StudentObligationView(APIView):
    def get(self, request):
        student_obligations = StudentObligation.objects.all()
        serializer = StudentObligationSerializer(student_obligations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentObligationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    

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


        student = Student(name=student_name, last_name=student_lastname, phone=student_phone, english_level=student_level, obligation_name=student_obligationname, obligation_datetime=student_obligationdate)
        student.save()
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'student.html', context)

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

def course(request):
    return render(request, 'course.html', {'course': course})


def schedule(request):
    return render(request, 'schedule.html', {'schedule': schedule})


#fetching data from database
