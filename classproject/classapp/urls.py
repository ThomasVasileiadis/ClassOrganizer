from django.contrib import admin
from django.urls import path, include
from classapp import views



urlpatterns = [
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('course/', views.course, name='course'),
    path('schedule/', views.schedule, name='schedule'),
    path('student/addstudent/', views.addstudent, name='addstudent'),
    path('editstudent/<int:student_id>/', views.editstudent, name='editstudent'),
    path('teacher/addteacher/', views.addteacher, name='addteacher'),
    path('course/course_info/', views.course_info, name='course_info'),
]