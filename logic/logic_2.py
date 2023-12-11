import sqlite3
import pandas as pd
import os

db_path = os.path.abspath('./classproject/db.sqlite3')
print(f'Database path: {db_path}')


#############################################STUDENTS#############################################

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Execute a query to fetch the data from a table
cursor.execute("SELECT * FROM classapp_student")

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Create a dataframe from the fetched rows
df_students = pd.DataFrame(rows)

# Close the cursor and the connection
cursor.close()
conn.close()

# Print the dataframe
print(df_students)

#############################################TEACHERS#############################################

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Execute a query to fetch the data from a table
cursor.execute("SELECT * FROM classapp_teacher")

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Create a dataframe from the fetched rows
df_teachers = pd.DataFrame(rows)

# Close the cursor and the connection
cursor.close()
conn.close()

# Print the dataframe
print(df_teachers)


#############################################COURSES#############################################

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Execute a query to fetch the data from a table
cursor.execute("SELECT * FROM classapp_course")

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Create a dataframe from the fetched rows
df_courses = pd.DataFrame(rows)

# Close the cursor and the connection
cursor.close()
conn.close()

# Print the dataframe
print(df_courses)

