# ------------------------------------------------------------------------------------------ #
# Title: assignment05
# Desc: This assignment demonstrates similar features as assignment 5 but is more complex.
# Change Log: (Who, When, What)
# RRoot,1/1/2030,Created Script
# Julia Westfall,05/20/24, edited the script from assignment05_julia_westfall
# ------------------------------------------------------------------------------------------ #

# These statements should allow us to use "exit"
from sys import exit
import json

# Define the Data Constants
FILE_NAME: str = '../assignment_07/Enrollments.json'
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


def output_error_messages(message: str, error: Exception = None):
    """
This function displays custom error messages to the user

    :param message:
    :param error:
    :return:
    """
    print(message)
    print(error)


class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list) -> list:
        """
  this function reads data from a json file and loads it into a list of Student objects


        :param file_name:
        :param student_data:
        :return:
        """
        try:
            # open the file using the given file path
            file = open(file_name, 'r')

            # load the data into file_data using the json library
            file_data = json.load(file)

            # close the file
            file.close()

            # append the new data to the students data list.
            # TODO: Add code to make sure there are not duplicate values in student_data after the append opp
            for student in file_data:
                student_data.append(student)

        # catch errors related to the file not being found
        except Exception as error:
            msg = 'something went wrong while reading data from file'
            output_error_messages(message=msg, error=error)
            return student_data

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list) -> None:
        """This function writes data to a json file with data f

        :param file_name:
        :param student_data:
        :return:
        """
        try:
            file = open(file_name, 'w')
            json.dump(student_data, file)
        except Exception as error:
            msg = 'There was an error with the write_data_to_file function'
            output_error_messages(message=msg, error=error)
        return None


class IO:
    """
 collection of presentation layer functions that manage user input and output
    """

    @staticmethod
    def input_student_data(students: list):
        """
his function gets the student's first name and last name, with a course name from the user
        :param students:
        :return:
        """
        try:
            student_first_name: str = input('Please enter the first name for the student ')
            student_last_name: str = input('Please enter the last name for the student ')
            course_name: str = input('Please enter the name of the course ')
            students_data: dict = {'FirstName': student_first_name, 'LastName': student_last_name,
                                   'CourseName': course_name}
            students.append(students_data)
        except Exception as error:
            msg = 'something went wrong while reading data from file'
            output_error_messages(message=msg, error=error)

        return students

    @staticmethod
    def output_student_courses(student_data: list):
        for student in student_data:
            temp_line: str = f"{student['FirstName']},{student['LastName']},{student['CourseName']}"
            print(temp_line)

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def input_menu_choice():
        return input('Please select an option from the menu: ')

    @staticmethod
    def __output_error_messages(message: str, error: Exception = None):
        print(message)
        print(error)


# initialize the class objects
input_output = IO()
file_opps = FileProcessor()

# Call function to read data from file
students = file_opps.read_data_from_file(FILE_NAME, students)

# As long as you have not quit the program, go to the "if statements"
while True:
    # Present the menu of choices
    input_output.output_menu(menu=MENU)

    # prompts user for menu selection
    menu_choice: str = input_output.input_menu_choice()

    # Input user data
    if menu_choice == '1':
        students = input_output.input_student_data(students)

    # Present the current data
    elif menu_choice == '2':
        input_output.output_student_courses(students)

        # Save the new data to a file
    elif menu_choice == '3':
        file_opps.write_data_to_file(FILE_NAME, students)

    # Stop the loop
    elif menu_choice == '4':
        exit()

    else:
        print('That value is not an option. Please enter 1,2,3, or 4')
