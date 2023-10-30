# student.py
from authentication import signin

# Authenticate user
if signin():
    # Read student data from students.txt
    with open("students.txt", "r") as file:
        student_data = file.readlines()

    # Display student data
    print("Student ID\tStudent Name\tStudent Age\tStudent Location")
    for data in student_data:
        print(data.strip())

    # Additional features (number of students, lowest and highest age)
    num_students = len(student_data)
    ages = [int(student.split('\t')[2]) for student in student_data]
    lowest_age = min(ages)
    highest_age = max(ages)

    print(f"No. of Students: {num_students}")
    print(f"Lowest Age of Student: {lowest_age}")
    print(f"Highest Age of Student: {highest_age}")
