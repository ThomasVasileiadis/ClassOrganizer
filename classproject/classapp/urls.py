from django.contrib import admin
from django.urls import path, include
from classapp import views



urlpatterns = [
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('course/', views.course, name='course'),
    path('schedule/', views.schedule, name='schedule'),
    path('student/student_info.html', views.student_info, name='student_info'),
    path('teacher/teacher_info.html', views.teacher_info, name='teacher_info'),
    path('course/course_info.html', views.course_info, name='course_info'),
]