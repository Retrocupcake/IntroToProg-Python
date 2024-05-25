# ------------------------------------------------------------------------------------------ #
# Title: assignment03
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Julia Westfall,05/05/24, edited the script from assignment03-starter
# ------------------------------------------------------------------------------------------ #

# These statements should allow us to use "if" statements and "exit"
from _ast import If
import sys

# Define the Data Constants
MENU: str = '''----Course Registration Program----
Select from the following menu:
1. Register a Student for a course
2. Show current data 
3. Save data to a file
4. Exit the program 
------------------------------'''

FILE_NAME: str = '../Assignments/Enrollments.csv'

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file_obj = None
menu_choice: str = ''
program_continue: bool = True

# Present the menu of choices
print(MENU)

while program_continue == True:
    menu_choice: str = input('Please select an option from the menu: ')

    # Input user data
    if menu_choice == '1':
        student_first_name: str = input('Please enter the first name for the student ')
        student_last_name: str = input('Please enter the last name for the student ')
        course_name: str = input('Please enter the name of the course ')
        csv_data: str = f"{student_first_name},{student_last_name},{course_name}\n"


    # Present the current data
    elif menu_choice == '2':
        # file_obj = open(FILE_NAME, 'r')
        # lines = file_obj.read()
        print(csv_data)

    # Save the new data to a file
    elif menu_choice == '3':
        file_obj = open(FILE_NAME, 'a')
        file_obj.write(csv_data)

        # This reads all data (including data recently added) then closes the file
        file_obj = open(FILE_NAME, 'r')
        lines = file_obj.read()
        file_obj.close()
        print(lines)

    # Stop the loop
    elif menu_choice == '4':
        program_continue = False

    else:
        print('That value is not an option. Please enter 1,2,3, or 4')
