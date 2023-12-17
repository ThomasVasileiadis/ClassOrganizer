from django.contrib import admin
from django.urls import path, include
from classapp import views



urlpatterns = [
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('course/', views.course, name='course'),
    path('schedule/', views.schedule, name='schedule'),
    path('student/addstudent/', views.addstudent, name='addstudent'),
    path('editstudent/', views.EditStudent.as_view(), name='editstudent'),
    path('deletestudent/', views.deletestudent, name='deletestudent'),
    path('editteacher/', views.EditTeacher.as_view(), name='editteacher'), # <int:teacher_id>/
    path('deleteteacher/', views.deleteteacher, name='deleteteacher'),
    path('teacher/addteacher/', views.addteacher, name='addteacher'),
    path('course/course_info/', views.course_info, name='course_info'),
    path('course/addcourse/', views.addcourse, name='addcourse'),
    path('editcourse/<int:course_id>/', views.editcourse, name='editcourse'),
    path('deletecourse/<int:course_id>/', views.deletecourse, name='deletecourse'),
]