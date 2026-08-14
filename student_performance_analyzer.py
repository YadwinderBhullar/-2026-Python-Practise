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
def each_students_average_marks(students):

    for name ,values in students.items():
        total = 0
        for marks in values:
            total= total + marks
        average =total /len(values)
        print(name,"average:",average)
each_students_average_marks(students)