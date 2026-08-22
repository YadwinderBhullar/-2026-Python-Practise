# ============================================
# TUPLE EMPLOYEE RECORDS PROJECT
# ============================================

employees = [
    ("John", "Sales", 5000),
    ("Sarah", "Marketing", 6000),
    ("Mike", "IT", 7000)
]


# ============================================
# 1. Display all employee records
# ============================================

def display_employees(employees):

    print("EMPLOYEE RECORDS")
    print("-" * 40)

    for name, department, salary in employees:
        print(f"{name:<15}{department:<15}${salary:,.2f}")


# ============================================
# 2. Calculate total number of employees
# ============================================

def count_employees(employees):

    count = 0

    for employee in employees:
        count += 1

    return count


# ============================================
# 3. Find the highest salary
# ============================================

def find_highest_salary(employees):

    highest = 0

    for name, department, salary in employees:

        if salary > highest:
            highest = salary

    return highest


# ============================================
# 4. Find the employee with the highest salary
# ============================================

def find_highest_paid_employee(employees):

    highest = 0
    highest_employee = ""

    for name, department, salary in employees:

        if salary > highest:
            highest = salary
            highest_employee = name

    return highest_employee


# ============================================
# 5. Calculate total salaries
# ============================================

def calculate_total_salaries(employees):

    total_salary = 0

    for name, department, salary in employees:
        total_salary += salary

    return total_salary


# ============================================
# 6. Calculate average salary
# ============================================

def calculate_average_salary(employees):

    total_salary = calculate_total_salaries(employees)
    number_of_employees = count_employees(employees)

    average_salary = total_salary / number_of_employees

    return average_salary


# ============================================
# 7. Find employees by department
# ============================================

def find_employees_by_department(employees, department):

    employees_found = []

    for name, employee_department, salary in employees:

        if employee_department == department:
            employees_found.append(name)

    return employees_found


# ============================================
# 8. Create employee report
# ============================================

def create_employee_report(employees):

    total_employees = count_employees(employees)
    total_salaries = calculate_total_salaries(employees)
    average_salary = calculate_average_salary(employees)
    highest_salary = find_highest_salary(employees)
    highest_paid_employee = find_highest_paid_employee(employees)

    departments = {}

    for name, department, salary in employees:

        if department not in departments:
            departments[department] = []

        departments[department].append(name)

    return {
        "total_employees": total_employees,
        "total_salaries": total_salaries,
        "average_salary": average_salary,
        "highest_salary": highest_salary,
        "highest_paid_employee": highest_paid_employee,
        "departments": departments
    }


# ============================================
# 9. Display employee report
# ============================================

def print_employee_report(report):

    print()
    print("=" * 40)
    print("       EMPLOYEE RECORDS REPORT")
    print("=" * 40)

    print()
    print("EMPLOYEE RECORDS")
    print("-" * 40)
    print(f"{'Employee':<15}{'Department':<15}Salary")
    print("-" * 40)

    for name, department, salary in employees:
        print(f"{name:<15}{department:<15}${salary:,.2f}")

    print()
    print("-" * 40)
    print(f"Total Employees: {report['total_employees']}")
    print(f"Total Salaries: ${report['total_salaries']:,.2f}")
    print(f"Average Salary: ${report['average_salary']:,.2f}")
    print(f"Highest Salary: ${report['highest_salary']:,.2f}")
    print(f"Highest Paid Employee: {report['highest_paid_employee']}")

    print()
    print("-" * 40)
    print("EMPLOYEES BY DEPARTMENT")
    print("-" * 40)

    for department, employee_names in report["departments"].items():

        print()
        print(f"{department}:")

        for name in employee_names:
            print(name)

    print()
    print("=" * 40)
    print("           END OF REPORT")
    print("=" * 40)


# ============================================
# MAIN PROGRAM
# ============================================


report = create_employee_report(employees)

print_employee_report(report)