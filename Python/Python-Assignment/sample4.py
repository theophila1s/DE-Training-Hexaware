import json

# Define JSON string
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'

# Convert JSON String to Python
student_details = json.loads(jsonString)

# Print Dictionary
print(student_details)

# Print values using keys
print(student_details['name'])
print(student_details['course'])


import json

# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)

# Print the type of data variable
print("Type:", type(data))

# Print the data of dictionary
print("\nPeople1:", data['people1'])
print("\nPeople2:", data['people2'])



import pandas as pd
import numpy as np
# Creating empty series
ser = pd.Series()
print("Pandas Series: ", ser)
# simple array
data = np.array(['H', 'e', 'x', 'a', 'a'])
ser = pd.Series(data)
print("Pandas Series:\n", ser)