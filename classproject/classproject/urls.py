"""
URL configuration for classproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from classapp.views import *
from classapp import views

urlpatterns = [
     path('admin/', admin.site.urls),
    #path('student/', StudentView.as_view(), name="student"),
    #path('teacher/', TeacherView.as_view(), name="teacher"),
    #path('course/', CourseView.as_view(), name="course"),
    #path('schedule/', ScheduleView.as_view(), name="schedule"),
    path('obligations/', ObligationsView.as_view(), name="obligations"),
    path('studentcourse/', StudentCourseView.as_view(), name="studentcourse"),
    path('studentobligation/', StudentObligationView.as_view(), name="studentobligation"),
    path('home/', views.home, name='home'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('course/', views.course, name='course'),
    path('schedule/', views.schedule, name='schedule'),
    path('student/student_info.html', views.student_info, name='student_info'),
    path('teacher/teacher_info.html', views.teacher_info, name='teacher_info'),
    path('course/course_info.html', views.course_info, name='course_info'),
]


#urlpatterns = [
#    path('student/', views.StudentList.as_view()),
#    path('student/<int:pk>/', views.StudentDetail.as_view()),
#    path('teacher/', views.TeacherList.as_view()),
#    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
#    path('course/', views.CourseList.as_view()),
#    path('course/<int:pk>/', views.CourseDetail.as_view()),
#    path('schedule/', views.ScheduleList.as_view()),
#    path('schedule/<int:pk>/', views.ScheduleDetail.as_view()),
#    path('obligations/', views.ObligationsList.as_view()),
#    path('obligations/<int:pk>/', views.ObligationsDetail.as_view()),
#    path('studentcourse/', views.StudentCourseList.as_view()),
#    path('studentcourse/<int:pk>/', views.StudentCourseDetail.as_view()),
#    path('studentobligation/', views.StudentObligationList.as_view()),
#    path('studentobligation/<int:pk>/', views.StudentObligationDetail.as_view()),
#]