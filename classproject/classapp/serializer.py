from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        class StudentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ObligationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obligations
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'

class StudentObligationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentObligation
        fields = '__all__'

