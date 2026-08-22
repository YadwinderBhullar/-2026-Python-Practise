# ============================================
# EMPLOYEE SALARY ANALYZER
# ============================================

employees = {
    "John": 5000,
    "Sarah": 7000,
    "Mike": 4000,
    "David": 8000,
    "Lisa": 6500
}


# ============================================
# 1. Get employee names
# ============================================

def get_employee_names(employees):

    employee_names = [
        name
        for name, salary in employees.items()
    ]

    return employee_names


# ============================================
# 2. Get employee salaries
# ============================================

def get_employee_salaries(employees):

    employee_salaries = [
        salary
        for name, salary in employees.items()
    ]

    return employee_salaries


# ============================================
# 3. Get high-salary employees
# ============================================

def get_high_salary_employees(employees):

    high_salary = {
        name: salary
        for name, salary in employees.items()
        if salary >= 6000
    }

    return high_salary


# ============================================
# 4. Calculate 10% salary increase
# ============================================

def calculate_salary_increase(employees):

    salary_increase = {
        name: round(salary * 1.10, 2)
        for name, salary in employees.items()
    }

    return salary_increase


# ============================================
# 5. Get low-salary employees
# ============================================

def get_low_salary_employees(employees):

    low_salary = {
        name: salary
        for name, salary in employees.items()
        if salary < 6000
    }

    return low_salary


# ============================================
# 6. Create final salary report
# ============================================

def create_salary_report(employees):

    employee_names = get_employee_names(employees)

    employee_salaries = get_employee_salaries(employees)

    high_salary = get_high_salary_employees(employees)

    salary_increase = calculate_salary_increase(employees)

    low_salary = get_low_salary_employees(employees)

    return {
        "employee_names": employee_names,
        "employee_salaries": employee_salaries,
        "high_salary": high_salary,
        "salary_increase": salary_increase,
        "low_salary": low_salary
    }


# ============================================
# 7. Print final report
# ============================================

def print_salary_report(report):

    print("=" * 50)
    print("          EMPLOYEE SALARY REPORT")
    print("=" * 50)

    print()
    print("EMPLOYEE NAMES")
    print("-" * 50)

    for name in report["employee_names"]:
        print(name)

    print()
    print("EMPLOYEE SALARIES")
    print("-" * 50)

    for name, salary in zip(
        report["employee_names"],
        report["employee_salaries"]
    ):
        print(f"{name:<15} ${salary:,.2f}")

    print()
    print("HIGH-SALARY EMPLOYEES")
    print("-" * 50)

    for name, salary in report["high_salary"].items():
        print(f"{name:<15} ${salary:,.2f}")

    print()
    print("10% SALARY INCREASE")
    print("-" * 50)

    for name, salary in report["salary_increase"].items():
        print(f"{name:<15} ${salary:,.2f}")

    print()
    print("LOW-SALARY EMPLOYEES")
    print("-" * 50)

    for name, salary in report["low_salary"].items():
        print(f"{name:<15} ${salary:,.2f}")

    print()
    print("=" * 50)
    print("             END OF REPORT")
    print("=" * 50)


# ============================================
# MAIN PROGRAM
# ============================================

report = create_salary_report(employees)

print_salary_report(report)