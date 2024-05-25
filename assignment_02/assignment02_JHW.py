# ------------------------------------------------------------------------------------------ #
# Title: assignment02
# Desc: This assignment demonstrates how to create a csv file and store strings in said file
# Change Log: (Who, When, What)
# Julia Westfall,4/22/24, Created Script
# ------------------------------------------------------------------------------------------ #

# Constants
COURSE_NAME: str = 'Python 100'
COURSE_PRICE: float = 999.98
STATE_TAX: float = .09
TOTAL_PRICE: float = COURSE_PRICE + COURSE_PRICE * STATE_TAX
FILE_NAME: str = '../Assignments/Enrollments.csv'

# Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file_obj = None

# Temporarily turn float variables into strings so we can use string concatenation
str(COURSE_PRICE)
str(STATE_TAX)
str(TOTAL_PRICE)

# Input Statements
student_first_name: str = input('Tell me your first name ')
student_last_name: str = input('Tell me your last name ')

# Output Statements
csv_data: str = f"{student_first_name},{student_last_name},{COURSE_NAME},{COURSE_PRICE},{TOTAL_PRICE}"
print(csv_data)

# File processing
file_obj = open(FILE_NAME, 'w')
file_obj.write(csv_data)
file_obj.close()
