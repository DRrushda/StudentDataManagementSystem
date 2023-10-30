# insert.py
from authentication import signin

# Authenticate user
if signin():
    # Get student details
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    student_age = input("Enter Student Age: ")
    student_location = input("Enter Student Location: ")

    # Write student details to students.txt
    with open("students.txt", "a") as file:
        file.write(f"{student_id}\t{student_name}\t{student_age}\t{student_location}\n")

    print("Student data inserted successfully.")
