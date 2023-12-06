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
    path('deletestudent/<int:student_id>/', views.deletestudent, name='deletestudent'),
    path('editteacher/<int:teacher_id>/', views.editteacher, name='editteacher'),
    path('deleteteacher/<int:teacher_id>/', views.deleteteacher, name='deleteteacher'),
    path('teacher/addteacher/', views.addteacher, name='addteacher'),
    path('course/course_info/', views.course_info, name='course_info'),
    path('course/addcourse/', views.addcourse, name='addcourse'),
    path('editcourse/<int:course_id>/', views.edit_course, name='editcourse'),
    path('deletecourse/<int:course_id>/', views.delete_course, name='deletecourse'),
]