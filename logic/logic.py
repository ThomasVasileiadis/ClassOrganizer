import os
import sqlite3
import pandas as pd
import numpy as np

# Define the database path
db_path = os.path.abspath('./classproject/db.sqlite3')
print(f'Database path: {db_path}')

# Function to fetch data from SQLite database and return as a dataframe
def fetch_data_from_db(table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute a query to fetch the data from a table
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Get column names from the cursor description
    column_names = [column[0] for column in cursor.description]

    # Create a dataframe from the fetched rows and set the column names
    df = pd.DataFrame(rows, columns=column_names)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return df

# Fetch data from the database
df_students = fetch_data_from_db('classapp_student')
df_teachers = fetch_data_from_db('classapp_teacher')
df_courses = fetch_data_from_db('classapp_course')

# Print the dataframes
print(df_students)
print(df_teachers)
print(df_courses)

# Extract relevant fields from the students dataframe
english_level = df_students['english_level']
obligation_name = df_students['obligation_name']

# Create a binary matrix for conflict detection
conflict_matrix = np.zeros((len(df_students), len(df_students)), dtype=bool)


# Define the time slots
time_slots_temp = pd.date_range(start='15:00', end='21:30', freq='15min').time
time_slots = time_slots_temp[::3]  # Select every third element

# Define the days
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Create an empty schedule
schedule = pd.DataFrame(index=time_slots, columns=days)

# For each course
for _, course in df_courses.iterrows():
    # Find a teacher who can teach the course
    teacher = df_teachers[df_teachers['courses'].str.contains(course['course_name'])].iloc[0]

    # Find a time slot where the teacher is available
    for day in days:
        for time_slot in time_slots:
            if str(time_slot) not in teacher['availability']:
                continue

            # Assign students to the course based on their English level and availability
            students = df_students[(df_students['english_level'] == course['level']) & (df_students['availability'].str.contains(str(time_slot)))]

            # If there are students who can take the course at this time slot
            if not students.empty:
                # Assign the course to the time slot
                schedule.loc[time_slot, day] = f"{course['course_name']} (Teacher: {teacher['name']}, Students: {', '.join(students['name'])})"
                break

print(schedule)