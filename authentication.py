# authentication.py

def signin():
    # Read stored credentials from file
    with open("credentials.txt", "r") as file:
        stored_username, stored_password = file.readline().strip().split(',')

    # User input for authentication
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check user input against stored credentials
    if username == stored_username and password == stored_password:
        return True
    else:
        print("Authentication failed. Please try again.")
        return False
