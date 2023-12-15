import pandas as pd
from django_pandas.io import read_frame
import pandas as pd
from importlib import import_module
from django.conf import settings
from django.apps import apps
from app.models import Student, Teacher, Course, Enrollment, Schedule, Obligations, StudentCourse, StudentObligation



# Define the time slots
time_slots = pd.date_range("09:00", "17:00", freq="1H").time

# Define the days
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Get all teachers
teachers = Teacher.objects.all()

# Create a list to store the data
data = []

# For each teacher, create a dictionary with the teacher's information and the courses they teach
for teacher in teachers:
    teacher_data = {
        'teacher_id': teacher.teacher_id,
        'name': teacher.name,
        'last_name': teacher.last_name,
        'phone': teacher.phone,
        'working_days': teacher.working_days,
        'courses': ', '.join(course.name for course in teacher.courses.all()),
    }
    data.append(teacher_data)

# Create a DataFrame from the data
df_teachers = pd.DataFrame(data)

# Get all courses
df_courses = read_frame(Course.objects.all())

# Create an empty schedule
schedule = pd.DataFrame(index=time_slots, columns=days)

# For each course
for _, course in df_courses.iterrows():
    # Find a teacher who can teach the course
    teacher = df_teachers[df_teachers['courses'].str.contains(course['course_name'])].iloc[0]

    # Find a time slot where the teacher is available
    # Define the df_students DataFrame
    df_students = pd.DataFrame()

    for day in days:
        for time_slot in time_slots:
            if str(time_slot) not in teacher['working_days']:
                continue

            # Assign students to the course based on their English level and availability
            students = df_students[(df_students['english_level'] == course['level']) & (df_students['availability'].str.contains(str(time_slot)))]

            # If there are students who can take the course at this time slot
            if not students.empty:
                # Assign the course to the time slot
                schedule.loc[time_slot, day] = f"{course['course_name']} (Teacher: {teacher['name']}, Students: {', '.join(students['name'])})"
                break

print(schedule)