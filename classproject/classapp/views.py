from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from .forms import TeacherForm, StudentForm, CourseForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Course, Teacher, Student
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import clear_url_caches, reverse
from django.db.models import Sum


def home(request):
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    courses_count = Course.objects.count()
    total_monthly_pay = Student.objects.aggregate(Sum('monthly_pay'))['monthly_pay__sum']
    return render(request, 'home.html', {'student_count': student_count, 'teacher_count': teacher_count, 'courses_count': courses_count, 'total_monthly_pay': total_monthly_pay})


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

        student = Student(monthly_pay=monthly_pay, student_id=student_id, name=student_name, last_name=student_lastname,
                          phone=student_phone, english_level=student_level, obligation_name=student_obligationname,
                          obligation_datetime=student_obligationdate)
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

        student = Student(monthly_pay=monthly_pay, name=student_name, last_name=student_lastname, phone=student_phone,
                          english_level=student_level, obligation_name=student_obligationname,
                          obligation_datetime=student_obligationdate)
        student.save()
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'addstudent.html', context)



class EditStudent(APIView):
    def get(self, request):
        student_id = request.GET.get('student_id')

        if request.GET.get('edit_btn'):
            student_model = Student.objects.get_student_model(student_id=student_id)[0]
            print(f"Retrieved student: {student_id}")
            return render(request, 'editstudent.html', {'student': student_model})
        else:
            Student.objects.delete_student(student_id=student_id)
            students = Student.objects.all()
            return render(request, 'student.html', {'data': students})

    def post(self, request):
        print(request.POST)
        student_id = request.POST.get('student_id')
        student_model = Student.objects.get_student_model(student_id=student_id)[0]
        form = StudentForm(request.POST, instance=student_model)  # , instance=teacher_model
        if form.is_valid():
            student = form.save(commit=False)  # Get an instance of the model without saving it to the database
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

            return redirect(reverse('student'))
        else:
            print(form.errors)


def teacher(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('name')
        teacher_lastname = request.POST.get('last_name')
        teacher_phone = request.POST.get('phone')
        teacher_workingdays = request.POST.getlist('working_days')
        teacher_workinghours = request.POST.get('working_hours')

        # Join the list into a string with a separator
        teacher_workingdays_str = ', '.join(teacher_workingdays)

        teacher = Teacher(name=teacher_name, last_name=teacher_lastname, phone=teacher_phone,
                          working_days=teacher_workingdays_str, working_hours=teacher_workinghours)
        teacher.save()
    data = Teacher.objects.all()
    context = {'data': data}
    return render(request, 'teacher.html', context)


class EditTeacher(APIView):
    def get(self, request):
        teacher_id = request.GET.get('teacher_id')

        if request.GET.get('edit_btn'):

            teacher_model = Teacher.objects.get_teacher_model(teacher_id=teacher_id)[0]
            print(f"Retrieved teacher: {teacher_id}")
            return render(request, 'editteacher.html', {'teacher': teacher_model})

        else:
            Teacher.objects.delete_teacher(teacher_id=teacher_id)
            teachers = Teacher.objects.all()
            return render(request, 'teacher.html', {'data': teachers})

    def post(self, request):
        print(request.POST)
        teacher_id = request.POST.get('teacher_id')
        teacher_model = Teacher.objects.get_teacher_model(teacher_id=teacher_id)[0]
        form = TeacherForm(request.POST, instance=teacher_model)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.name = form.cleaned_data['name']
            teacher.last_name = form.cleaned_data['last_name']
            teacher.phone = form.cleaned_data['phone']
            teacher.working_days = ','.join(request.POST.getlist('working_days'))
            working_hours = form.cleaned_data.get('working_hours')  # Use get instead of calling the dictionary

            if working_hours is not None:
                teacher.working_hours = working_hours
            else:
                teacher.working_hours = " "  # default value

            teacher.save()
            print(f"Updated teacher: {teacher}")
            return redirect(reverse('teacher'))
        else:
            print(form.errors)


def addteacher(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('name')
        teacher_lastname = request.POST.get('last_name')
        teacher_phone = request.POST.get('phone')
        teacher_workingdays = request.POST.getlist('working_days')

        # Join the list into a string with a separator
        teacher_workingdays_str = ', '.join(teacher_workingdays)

        teacher = Teacher(name=teacher_name, last_name=teacher_lastname, phone=teacher_phone,
                          working_days=teacher_workingdays_str)
        teacher.save()
    data = Teacher.objects.all()
    context = {'data': data}

    return render(request, 'addteacher.html', context)


def course(request):
    if request.method == 'POST':
        course_name = request.POST.get('name')
        course_code = request.POST.get('code')
        course_description = request.POST.get('description')
        course_teacher_id = request.POST.get('teacher_id')

        try:
            teacher = Teacher.objects.get(teacher_id=course_teacher_id)
            course = Course(name=course_name, code=course_code, description=course_description, teacher=teacher)
            course.save()
        except ObjectDoesNotExist:
            pass

    data = Course.objects.all()
    context = {'data': data}

    return render(request, 'course.html', context)


def addcourse(request):
    if request.method == 'POST':
        course_name = request.POST.get('name')
        course_code = request.POST.get('code')
        course_description = request.POST.get('description')
        course_teacher = request.POST.get('teacher_id')

        course = Course(name=course_name, code=course_code, description=course_description, teacher_id=course_teacher)
        course.save()

    data = Course.objects.all()
    teachers = Teacher.objects.all()  # query all teachers
    context = {'data': data, 'teachers': teachers}  # add teachers to the context

    return render(request, 'addcourse.html', context)


def editcourse(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    print(f"Retrieved course: {course}")
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.name = form.cleaned_data['name']
            course.code = form.cleaned_data['code']
            course.description = form.cleaned_data['description']
            if 'teacher' in form.cleaned_data:  # Check if teacher is in form.cleaned_data
                course.teacher_id = form.cleaned_data['teacher']
            else:
                print("Teacher field is required.")
                return render(request, 'editcourse.html', {'form': form, 'course': course, 'teachers': teachers})
            course.save()
            print(f"Updated course: {course}")
            courses = Course.objects.all()
            return render(request, 'course.html', {'course_id': course.course_id, 'data': courses})
    else:
        form = CourseForm(instance=course)
    print(f"Form errors: {form.errors}")
    teachers = Teacher.objects.all()  # Query all teachers
    return render(request, 'editcourse.html',
                  {'form': form, 'course': course, 'teachers': teachers})  # Add teachers to the context

def deletestudent(request):
    student_id = request.GET.get('student_id')
    Student.objects.delete_student(student_id)
    return HttpResponseRedirect('/classapp/student')

def deleteteacher(request):
    teacher_id = request.GET.get('teacher_id')
    Teacher.objects.delete_teacher(teacher_id)
    return HttpResponseRedirect('/classapp/teacher')


def deletecourse(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)  # Use course_id instead of id
    course.delete()
    return redirect('course')


# GENERATION OF SCHEDULE
def schedule(request):
    return render(request, 'schedule.html', {'schedule': schedule})


def student_info(request):
    return render(request, 'student_info.html', {'student_info': student_info})


def teacher_info(request):
    return render(request, 'teacher_info.html', {'teacher_info': teacher_info})


def course_info(request):
    return render(request, 'course_info.html', {'course_info': course_info})
