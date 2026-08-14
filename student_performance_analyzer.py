""" Your program should determine:

Each student's average mark
Whether they passed or failed
The student with the highest average
The student with the lowest average """

students = {
    "John": [78, 85, 92],
    "Mike": [45, 55, 60],
    "Sarah": [90, 95, 88],
    "David": [35, 42, 48]
}
def each_students_average_marks(marks):

    total = 0
    for mark in marks:
         total= total + mark

    return total /len(marks)
        



def check_student_pass_or_fail(average):

    

    if average >= 50:
        result = "pass"
    else:
        result = "fail"



def highest_average(students):
    highest_average = 0
    student_name=""
    for name, marks in students.items():
        average = each_students_average_marks(marks)

        if average >highest_average:
             highest_average = average  
             student_name = name
    return student_name, highest_average


def lowest_average(students):
    lowest_average = 999
    student_name=""
    for name, marks in students.items():
        average = each_students_average_marks(marks)
        if average < lowest_average:
             lowest_average = average  
             student_name = name
    return student_name , lowest_average

for name,marks in students.items():
    average =each_students_average_marks(marks)
    result =check_student_pass_or_fail(average)

    print(
        name,
        "-Average",
        round(average,2),
        "-",
        result
    )



highest_student, highest_mark = highest_average(students)
lowest_student, lowest_mark = lowest_average(students)


print("\nHighest Average:")
print(highest_student, "-", round(highest_mark, 2))

print("\nLowest Average:")
print(lowest_student, "-", round(lowest_mark, 2))