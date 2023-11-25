from django.contrib import admin
from django.urls import path, include
from classapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentView.as_view(), name="student"),
    path('teacher/', TeacherView.as_view(), name="teacher"),
    path('course/', CourseView.as_view(), name="course"),
    path('schedule/', ScheduleView.as_view(), name="schedule"),
    path('obligations/', ObligationsView.as_view(), name="obligations"),
    path('studentcourse/', StudentCourseView.as_view(), name="studentcourse"),
    path('studentobligation/', StudentObligationView.as_view(), name="studentobligation"),
]