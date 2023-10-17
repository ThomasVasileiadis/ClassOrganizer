"""
This script generates test data for 100 students, preprocesses the data into one-hot encoding for days and times, 
creates a binary matrix for conflict detection, builds a neural network model with output units matching the dimensions 
of availability, trains the model on the availability data, uses the model to predict the schedule, applies the conflict 
matrix to the schedule to ensure no conflicts, groups students based on their availability and English level, and assigns 
each group to a class. 

The script imports the following libraries:
    - numpy
    - pandas
    - tensorflow
    - Faker

The script defines the following functions:
    - None

The script includes the following main steps:
    1. Generate test data for 100 students
    2. Convert the data to a Pandas DataFrame and save it to a CSV file
    3. Load and preprocess student data from a CSV file
    4. Preprocess data into one-hot encoding for days and times
    5. Create a binary matrix for conflict detection
    6. Fill the conflict matrix based on student constraints
    7. Cast the conflict matrix to boolean
    8. Cast data types to 'float32'
    9. Build a neural network model with output units matching the dimensions of availability
    10. Define the model
    11. Compile the model
    12. Train the model on the availability data
    13. Use the model to predict the schedule
    14. Apply the conflict matrix to the schedule to ensure no conflicts
    15. Group students based on their availability and English level
    16. Assign each group to a class
"""
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from faker import Faker

# Generate test data for 100 students
fake = Faker()
data = []
for i in range(70):
    name = fake.name()
    availability = fake.random_elements(elements=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'), length=2, unique=True)
    availability_str = '; '.join([f"{day} {fake.random_element(elements=('15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00'))}-" \
                                  f"{fake.random_element(elements=('17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'))}" \
                                  for day in availability])
    other_activities = fake.random_element(elements=('Swimming', 'Chess', 'Reading', 'Writing', 'Drawing', 'Music', 'Dancing'))
    english_level = fake.random_element(elements=('Pre-Junior', 'A-Junior', 'A', 'B', 'C', 'D', 'E', 'Lower', 'Proficiency'))
    data.append([name, availability_str, other_activities, english_level])

# Convert the data to a Pandas DataFrame and save it to a CSV file
df = pd.DataFrame(data, columns=['Student Name', 'Availability', 'Other Activities', 'English Level'])
df.to_csv('C:\\Users\\melen\\Desktop\\ClassOrganizer\\logic\\student_data.csv', index=False)

# Load and preprocess student data from a CSV file
data = pd.read_csv("C:\\Users\\melen\\Desktop\\ClassOrganizer\\logic\\student_data.csv")

# Example data columns: 'Student Name', 'Availability', 'Other Activities', 'English Level'

# Preprocess data into one-hot encoding for days and times
availability = pd.get_dummies(data['Availability'], prefix='day_time')
other_activities = data['Other Activities']

# Create a binary matrix for conflict detection
conflict_matrix = np.zeros((len(data), len(data)), dtype=bool)

# Fill the conflict matrix based on student constraints
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if other_activities[i] == other_activities[j]:
            conflict_matrix[i, j] = True
            conflict_matrix[j, i] = True

# Cast the conflict matrix to boolean
conflict_matrix = conflict_matrix.astype(bool)

# Cast data types to 'float32'
availability = availability.astype(np.float32)

# Build a neural network model with output units matching the dimensions of availability
input_layer = Input(shape=(len(availability.columns),))
hidden_layer = Dense(64, activation='relu')(input_layer)
output_layer = Dense(len(availability.columns), activation='softmax')(hidden_layer)

# Define the model
model = Model(inputs=input_layer, outputs=output_layer)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Train the model on the availability data
model.fit(availability, availability, epochs=10, batch_size=32)

# Use the model to predict the schedule
schedule = model.predict(availability)

# Apply the conflict matrix to the schedule to ensure no conflicts
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if conflict_matrix[i, j]:
            schedule[i, np.argmax(schedule[j])] = 0

# Define a list of days and times
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
times = ['15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00']

# Group students based on their availability and English level
groups = {}
for i in range(len(data)):
    availability_str = data.iloc[i]['Availability']
    english_level = data.iloc[i]['English Level']
    if english_level not in groups:
        groups[english_level] = []
    groups[english_level].append(data.iloc[i]['Student Name'])

# Assign each group to a class
class_num = 1
for english_level, group in groups.items():
    num_students = len(group)
    num_classes = (num_students // 7) + (1 if num_students % 7 > 0 else 0)
    for i in range(num_classes):
        class_size = min(num_students - i * 7, 7)
        class_group = group[i * 7:i * 7 + class_size]
        print(f"Class {class_num} ({english_level}): {', '.join(class_group)}")
        class_num += 1

## Print the schedule with class information
#print("Schedule:")
#for i in range(len(data)):
#    class_num = 0
#    for availability_str, level_groups in groups.items():
#        for english_level, group in level_groups.items():
#            if data.iloc[i]['Student Name'] in group:
#                class_num += 1
#                print(f"{data.iloc[i]['Student Name']} (Class {class_num}): {', '.join([days[j] + ' ' + times[np.argmax(schedule[i, j * len(times):(j + 1) * len(times)])] for j in range(len(days)) if np.max(schedule[i, j * len(times):(j + 1) * len(times)]) > 0])}")