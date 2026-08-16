employees = {
    "John": {
        "department": "Sales",
        "sales": [12000, 15000, 11000],
        "hours": 160
    },

    "Sarah": {
        "department": "Sales",
        "sales": [18000, 21000, 19500],
        "hours": 175
    },

    "Mike": {
        "department": "Marketing",
        "sales": [9000, 12000, 10000],
        "hours": 150
    },

    "David": {
        "department": "Marketing",
        "sales": [15000, 14000, 16000],
        "hours": 165
    }
}


# 1. Calculate total sales for one employee
def calculate_total_sales(sales):
    total = 0

    for sale in sales:
        total = total + sale

    return total


# 2. Calculate sales per hour
def calculate_sales_per_hour(sales, hours):
    total = calculate_total_sales(sales)
    sales_per_hour = total / hours

    return sales_per_hour


# 3. Analyze one employee
def analyze_employee( data):

    sales = data["sales"]
    hours = data["hours"]

    total_sales = calculate_total_sales(sales)
    sales_per_hour = calculate_sales_per_hour(sales, hours)

    return total_sales, sales_per_hour


# 4. Determine performance
def determine_performance(sales_per_hour):
    if sales_per_hour >= 300:
        return "Excellent"

    elif sales_per_hour >= 250:
        return "Good"

    elif sales_per_hour >= 200:
        return "Average"

    else:
        return "Needs Improvement"


# 5. Calculate bonus
def calculate_bonus(total_sales, performance):
    if performance == "Excellent":
        return total_sales * 0.15

    elif performance == "Good":
        return total_sales * 0.10

    elif performance == "Average":
        return total_sales * 0.05

    else:
        return 0


# 6. Find top performer
def calculate_top_performer(employees):

    highest_sales_per_hour = 0
    top_employee = ""

    for name, data in employees.items():

        _, sales_per_hour = analyze_employee(data)

        if sales_per_hour > highest_sales_per_hour:
            highest_sales_per_hour = sales_per_hour
            top_employee = name

    return highest_sales_per_hour, top_employee


# 7. Find lowest performer
def calculate_lowest_performer(employees):
    lowest_sales_per_hour = 999999
    lowest_employee = ""

    for  name, data in employees.items():
        _, sales_per_hour = analyze_employee(data)

        if sales_per_hour < lowest_sales_per_hour:
            lowest_sales_per_hour = sales_per_hour
            lowest_employee = name

    return lowest_sales_per_hour, lowest_employee


# 8. Calculate company sales and total bonuses
def calculate_company_summary(employees):
    total_sales = 0
    total_bonus = 0

    for data in employees.values():
        total, sales_per_hour = analyze_employee(data)

        performance = determine_performance(sales_per_hour)
        bonus = calculate_bonus(total, performance)

        total_sales += total
        total_bonus += bonus

    return total_sales, total_bonus


# 9. Calculate department sales
def calculate_department_sales(employees):
    department_sales = {}

    for data in employees.values():
        department = data["department"]

        total, _ = analyze_employee(data)

        if department not in department_sales:
            department_sales[department] = 0

        department_sales[department] += total
        

    return department_sales


# 10. Find best department by total sales
def calculate_best_department(department_sales):

    highest_sales = 0
    best_department = ""

    for department, sales in department_sales.items():

        if sales > highest_sales:
            highest_sales = sales
            best_department = department

    return best_department, highest_sales


# 11. Calculate department average sales
def calculate_department_average(employees):
    department_sales = {}
    department_count = {}

    for data in employees.values():

        department = data["department"]

        total, _ = analyze_employee(data)

        if department not in department_sales:
            department_sales[department] = 0
            department_count[department] = 0

        department_sales[department] += total
        department_count[department] += 1

    department_average = {}

    for department in department_sales:
        department_average[department] = (
            department_sales[department]
            / department_count[department]
        )

    return department_average


# 12. Find best department by average sales
def find_best_department_by_average(averages):
    highest_average = 0
    best_department = ""

    for department, average in averages.items():

        if average > highest_average:
            highest_average = average
            best_department = department

    return highest_average, best_department

# 14. Calcualte Performance Statistics
def calculate_performance_statistics(employees):

    statistics = {
        "Excellent": 0,
        "Good": 0,
        "Average": 0,
        "Needs Improvement": 0
    }

    for  data in employees.values():

        total, sales_per_hour = analyze_employee(data)

        performance = determine_performance(sales_per_hour)

        statistics[performance] += 1

    return statistics

# Calculate statistics once
statistics = calculate_performance_statistics(employees)

# We already have the Excellent count here.
excellent_count = statistics["Excellent"]

print("Excellent employees:", excellent_count)



# 15. Calculate Performance Distribution Report
def print_performance_report(statistics):

    print("========== PERFORMANCE DISTRIBUTION ==========")
    print()

    for performance, count in statistics.items():
        print(performance, ":", count)


statistics = calculate_performance_statistics(employees)

print_performance_report(statistics) 

# 16. Calculate Performance Percentage
def calculate_performance_percentages(statistics, total_employees):

    print("========== PERFORMANCE PERCENTAGE ==========")
    print()

    percentages={

    }
    for performance, count in statistics.items():

        percentage = (count / total_employees)*100
        percentages[performance] = percentage
    return percentages

statistics = calculate_performance_statistics(employees)

total_employees = len(employees)

percentages = calculate_performance_percentages(
    statistics,
    total_employees
)

print("========== PERFORMANCE PERCENTAGE ==========")
print()

for performance, percentage in percentages.items():
    print(performance, ":", round(percentage, 2), "%")



    




    


# ==============================
# EMPLOYEE REPORT
# ==============================

print("\n========== EMPLOYEE REPORT ==========\n")

for name, data in employees.items():

    total, rate = analyze_employee(data)

    performance = determine_performance(rate)

    bonus = calculate_bonus(total, performance)

    print("Employee:", name)
    print("Department:", data["department"])
    print("Total sales:", "$", round(total, 2))
    print("Sales per hour:", "$", round(rate, 2))
    print("Performance:", performance)
    print("Bonus:", "$", round(bonus, 2))
    print()


# ==============================
# COMPANY SUMMARY
# ==============================

company_sales, company_bonus = calculate_company_summary(employees)

top_rate, top_employee = calculate_top_performer(employees)

lowest_rate, lowest_employee = calculate_lowest_performer(employees)


print("========== COMPANY SUMMARY ==========\n")

print("Total company sales:", "$", round(company_sales, 2))
print("Total company bonus:", "$", round(company_bonus, 2))

print(
    "Average sales per hour:",
    "$",
    round(
        sum(
            calculate_sales_per_hour(
                data["sales"],
                data["hours"]
            )
            for data in employees.values()
        ) / len(employees),
        2
    )
)

print("Top performer:", top_employee)
print("Top sales per hour:", "$", round(top_rate, 2))

print("Lowest performer:", lowest_employee)
print("Lowest sales per hour:", "$", round(lowest_rate, 2))

print("Excellent employees:", excellent_count)


# ==============================
# DEPARTMENT SUMMARY
# ==============================

department_sales = calculate_department_sales(employees)

best_department, best_department_sales = calculate_best_department(
    department_sales
)

department_averages = calculate_department_average(employees)

best_average, best_average_department = find_best_department_by_average(
    department_averages
)


print("\n========== DEPARTMENT SUMMARY ==========\n")

for department, sales in department_sales.items():
    print(
        department,
        "Total Sales: $",
        round(sales, 2),
        "Average/Employee: $",
        round(department_averages[department], 2)
    )

print("\nBest department by total sales:", best_department)
print("Department sales:", "$", round(best_department_sales, 2))

print(
    "Best department by average sales:",
    best_average_department
)

print("Average sales:", "$", round(best_average, 2))





