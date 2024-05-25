# ------------------------------------------------------------------------------------------ #
# Title: assignment04
# Desc: This assignment demonstrates using conditional logic and looping and lists
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Julia Westfall,05/05/24, edited the script from assignment03_julia_westfall
# ------------------------------------------------------------------------------------------ #

# These statements should allow us to use "if" statements and "exit"
from _ast import If
import sys

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
csv_data: str = ''
file = None
menu_choice: str = ''
student_data: list = []
students: list = []

# Behind the scenes will create a new file named enrollments (or open if exists)
file = open(FILE_NAME, 'r')

# creates new variable that reads the enrollments file
csv_data = file.read()

# closes the file
file.close()

# This variable splits each line into separate lists by the new lines /n
lines = csv_data.split('\n')

# Saying for an element in lines variable (which is a line in this case) add student data to it
# in the form of a list instead of a string (as long as string is not equal to empty string)
for line in lines:
    if line is not '':
        student_data.append(line.split(','))

# As long as you have not quit the program, go to the "if statements"
while True:
    # Present the menu of choices
    print(MENU)

    # prompts user for menu selection
    menu_choice: str = input('Please select an option from the menu: ')

    # Input user data
    if menu_choice == '1':
        student_first_name: str = input('Please enter the first name for the student ')
        student_last_name: str = input('Please enter the last name for the student ')
        course_name: str = input('Please enter the name of the course ')
        students_list: list = [student_first_name, student_last_name, course_name]
        student_data.append(students_list)

    # Present the current data
    elif menu_choice == '2':
        for student in student_data:
            temp_line: str = f'{student[0]},{student[1]},{student[2]}'
            print(temp_line)

    # Save the new data to a file
    elif menu_choice == '3':
        file = open(FILE_NAME, 'w')
        for student in student_data:
            temp_line: str = f'{student[0]},{student[1]},{student[2]}\n'

            file.write(temp_line)

        file.close()

    # Stop the loop
    elif menu_choice == '4':
        exit()

    else:
        print('That value is not an option. Please enter 1,2,3, or 4')