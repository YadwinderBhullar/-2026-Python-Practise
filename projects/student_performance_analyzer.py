"""
Student Performance Analyzer

The program determines:
1. Each student's average mark
2. Whether they passed or failed
3. The student with the highest average
4. The student with the lowest average
"""

students = {
    "John": [78, 85, 92],
    "Mike": [45, 55, 60],
    "Sarah": [90, 95, 88],
    "David": [35, 42, 48]
}


# Calculate the average marks for one student
def calculate_average(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total / len(marks)


# Check whether a student passed or failed
def check_pass_fail(average):
    if average >= 50:
        return "PASS"
    else:
        return "FAIL"


# Find the student with the highest average
def find_highest_average(students):
    highest_average = 0
    highest_student = ""

    for name, marks in students.items():
        average = calculate_average(marks)

        if average > highest_average:
            highest_average = average
            highest_student = name

    return highest_student, highest_average


# Find the student with the lowest average
def find_lowest_average(students):
    lowest_average = 999
    lowest_student = ""

    for name, marks in students.items():
        average = calculate_average(marks)

        if average < lowest_average:
            lowest_average = average
            lowest_student = name

    return lowest_student, lowest_average


# ==========================
# STUDENT REPORT
# ==========================

print("========== STUDENT REPORT ==========\n")

for name, marks in students.items():

    average = calculate_average(marks)
    result = check_pass_fail(average)

    print("Student:", name)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Result:", result)
    print()


# ==========================
# HIGHEST AND LOWEST
# ==========================

highest_student, highest_average = find_highest_average(students)

lowest_student, lowest_average = find_lowest_average(students)


print("========== CLASS SUMMARY ==========\n")

print(
    "Highest average:",
    highest_student,
    "-",
    round(highest_average, 2)
)

print(
    "Lowest average:",
    lowest_student,
    "-",
    round(lowest_average, 2)
)