# ------------------------------------------------------------------------------------------ #
# Title: assignment05
# Desc: This assignment demonstrates similar features as assignment 4. It shows dictionaries and Error Handling,too.
# Change Log: (Who, When, What)
# RRoot,1/1/2030,Created Script
# Julia Westfall,05/20/24, edited the script from assignment04_julia_westfall
# ------------------------------------------------------------------------------------------ #

# These statements should allow us to use "exit"
from sys import exit

# Define the Data Constants
FILE_NAME: str = 'Enrollments.csv'
MENU: str = '''----Course Registration Program----
Select from the following menu:
1. Register a Student for a course
2. Show current data 
3. Save data to a file
4. Exit the program 
------------------------------'''

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: list = []
file = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

# Behind the scenes will create a new file named enrollments (or open if exists)
try:
    file = open(FILE_NAME, 'r')

    # creates new variable that reads the enrollments file
    csv_data = file.readlines()

    # closes the file
    file.close()
except FileNotFoundError:
    print('File Not Found')

# Saying for an element in lines variable (which is a line in this case) add student data to it
# in the form of a list instead of a string (as long as string is not equal to empty string)
for line in csv_data:
    try:
        if line is not '':
            line_elements = line.strip().split(',')
            starter_dict = {'first name': line_elements[0], 'last name': line_elements[1], 'course name': line_elements[2]}
            students.append(starter_dict)
    except IndexError as error:
        print(f'The csv line "{line}" does not contain the correct number of elements: {error}')

# As long as you have not quit the program, go to the "if statements"
while True:
    # Present the menu of choices
    print(MENU)

    # prompts user for menu selection
    menu_choice: str = input('Please select an option from the menu: ')

    # Input user data
    if menu_choice == '1':
        try:
            student_first_name: str = input('Please enter the first name for the student ')
            student_last_name: str = input('Please enter the last name for the student ')
            course_name: str = input('Please enter the name of the course ')
            students_data: dict = {'first name': student_first_name, 'last name': student_last_name,
                                   'course name': course_name}
            students.append(students_data)
        except TypeError as error:
            print(error)

    # Present the current data
    elif menu_choice == '2':
        for student in students:
            temp_line: str = f"{student['first name']},{student['last name']},{student['course name']}"
            print(temp_line)

        # Save the new data to a file
    elif menu_choice == '3':
        try:
            file = open(FILE_NAME, 'w')
            for student in students:
                temp_line: str = f"{student['first name']},{student['last name']},{student['course name']}\n"
                file.write(temp_line)
                print(temp_line.strip())
            file.close()
        except IOError:
            print('File Not Found or this program does not have permissions to write to the specified file')

    # Stop the loop
    elif menu_choice == '4':
        exit()

    else:
        print('That value is not an option. Please enter 1,2,3, or 4')
