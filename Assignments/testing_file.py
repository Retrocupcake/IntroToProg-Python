#
# student_row1: dict[str, str] = {'first_name':'Julia', 'last_name':'Westfall','course_name':'Python lvl 1'}
# student_row2: dict[str, str] = {'first_name':'Drew', 'last_name':'Pienta','course_name':'Python1000'}
# students: list[dict[str,str]] = [student_row1, student_row2]
#
# for row in students:
#
#     srow3: dict[str, str] = {'first_name':student_first_name,'last_name': student_last_name, 'course_name': course_name}
#     students.append(srow3)
#
# for row in students:
#     print  (f'{row["first_name"]}{row["last_name"]}{row["course_name"]}')
#
#


all_lists=[]
student_first_name: str = input('Please enter the first name for the student ')
student_last_name: str = input('Please enter the last name for the student ')
course_name: str = input('Please enter the name of the course ')
ex_dict = {'First Name':student_first_name,'Last Name':student_last_name, 'Course Name':course_name}
print(ex_dict)

all_lists.append(ex_dict)



line_elements=[strings ]