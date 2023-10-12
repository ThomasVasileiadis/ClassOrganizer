import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# Generate random data
n_samples = 10000
obligations = np.random.choice(['podosfairo', 'family', 'other'], size=n_samples)
obligation_start_time = pd.to_timedelta(np.random.randint(1, 24, size=n_samples), unit='h')
obligation_end_time = obligation_start_time + pd.to_timedelta(np.random.randint(1, 4, size=n_samples), unit='h')
obligation_duration = obligation_end_time - obligation_start_time
class_time = pd.to_datetime(np.random.randint(15, 21, size=n_samples), unit='h').strftime('%H:%M')
class_duration = 45
day = np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], size=n_samples)
teacher = np.random.choice(['teacher1', 'teacher2', 'teacher3', 'teacher4', 'teacher5'], size=n_samples)
student = np.random.choice(['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7'], size=n_samples)

# Save data to dataframe
data = {'student': student, 'obligations': obligations, 'obligation_start_time': obligation_start_time, 'obligation_end_time': obligation_end_time, 'obligation_duration': obligation_duration, 'class_time': class_time, 'class_duration': class_duration, 'day': day, 'teacher': teacher, }
df = pd.DataFrame(data)

# Export data to CSV
current_path = os.getcwd()
df.to_csv(current_path + '/logic/training_data.csv', index=False)





