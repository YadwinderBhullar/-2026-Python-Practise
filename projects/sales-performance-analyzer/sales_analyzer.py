sales_data = [
    {
        "employee": "John",
        "department": "Electronics",
        "region": "East",
        "product": "Laptop",
        "units": 8,
        "unit_price": 1200,
        "hours": 40,
        "target": 9000
    },
    {
        "employee": "John",
        "department": "Electronics",
        "region": "East",
        "product": "Phone",
        "units": 15,
        "unit_price": 800,
        "hours": 40,
        "target": 10000
    },
    {
        "employee": "Sarah",
        "department": "Electronics",
        "region": "West",
        "product": "Laptop",
        "units": 10,
        "unit_price": 1200,
        "hours": 45,
        "target": 11000
    },
    {
        "employee": "Sarah",
        "department": "Electronics",
        "region": "West",
        "product": "Tablet",
        "units": 12,
        "unit_price": 500,
        "hours": 45,
        "target": 6000
    },
    {
        "employee": "Mike",
        "department": "Furniture",
        "region": "East",
        "product": "Desk",
        "units": 7,
        "unit_price": 300,
        "hours": 38,
        "target": 2500
    },
    {
        "employee": "Mike",
        "department": "Furniture",
        "region": "East",
        "product": "Chair",
        "units": 15,
        "unit_price": 150,
        "hours": 38,
        "target": 2000
    },
    {
        "employee": "David",
        "department": "Furniture",
        "region": "West",
        "product": "Desk",
        "units": 5,
        "unit_price": 300,
        "hours": 35,
        "target": 2000
    },
    {
        "employee": "David",
        "department": "Furniture",
        "region": "West",
        "product": "Chair",
        "units": 10,
        "unit_price": 150,
        "hours": 35,
        "target": 1800
    },
    {
        "employee": "Lisa",
        "department": "Electronics",
        "region": "East",
        "product": "Phone",
        "units": 20,
        "unit_price": 800,
        "hours": 42,
        "target": 12000
    },
    {
        "employee": "Lisa",
        "department": "Electronics",
        "region": "East",
        "product": "Tablet",
        "units": 8,
        "unit_price": 500,
        "hours": 42,
        "target": 4000
    },
    {
        "employee": "Robert",
        "department": "Furniture",
        "region": "West",
        "product": "Desk",
        "units": 9,
        "unit_price": 300,
        "hours": 40,
        "target": 2500
    },
    {
        "employee": "Robert",
        "department": "Furniture",
        "region": "West",
        "product": "Chair",
        "units": 20,
        "unit_price": 150,
        "hours": 40,
        "target": 2500
    },
    {
        "employee": "Emma",
        "department": "Electronics",
        "region": "North",
        "product": "Laptop",
        "units": 4,
        "unit_price": 1200,
        "hours": 36,
        "target": 6000
    },
    {
        "employee": "Emma",
        "department": "Electronics",
        "region": "North",
        "product": "Phone",
        "units": 10,
        "unit_price": 800,
        "hours": 36,
        "target": 7000
    },
    {
        "employee": "Daniel",
        "department": "Furniture",
        "region": "North",
        "product": "Desk",
        "units": 3,
        "unit_price": 300,
        "hours": 32,
        "target": 1500
    }
]


# ============================================
# STAGE 1 - BASIC CALCULATIONS
# ============================================


# 1. Count number of sales records
def count_sales_records(sales_data):

    count = 0

    for sale in sales_data:
        count += 1

    return count


# 2. Calculate total units sold
def calculate_total_units(sales_data):

    total_units = 0

    for sale in sales_data:
        total_units += sale["units"]

    return total_units


# 3. Calculate total sales revenue
def calculate_total_sales(sales_data):

    total_sales = 0

    for sale in sales_data:

        total_sale = sale["units"] * sale["unit_price"]

        total_sales += total_sale

    return total_sales


# 4. Calculate average sales revenue
def average_sales_revenue(total_sales, sales_data):

    average = total_sales / len(sales_data)

    return average


# 5. Find highest sales revenue
def find_highest_sales(sales_data):

    highest_sale = 0

    for sale in sales_data:

        total_sale = sale["units"] * sale["unit_price"]

        if total_sale > highest_sale:
            highest_sale = total_sale

    return highest_sale


# 6. Find lowest sales revenue
def find_lowest_sale(sales_data):

    lowest_sale = 999999999

    for sale in sales_data:

        total_sale = sale["units"] * sale["unit_price"]

        if total_sale < lowest_sale:
            lowest_sale = total_sale

    return lowest_sale


# ============================================
# STAGE 2 - EMPLOYEE ANALYSIS
# ============================================


# 7. Calculate total sales for each employee
def calculate_employee_sales(sales_data):

    total_sales = {}

    for sale in sales_data:

        name = sale["employee"]

        sale_amount = sale["units"] * sale["unit_price"]

        if name not in total_sales:
            total_sales[name] = sale_amount

        else:
            total_sales[name] += sale_amount

    return total_sales


# 8. Calculate total units for each employee
def calculate_employee_units(sales_data):

    total_units = {}

    for sale in sales_data:

        name = sale["employee"]

        units = sale["units"]

        if name not in total_units:
            total_units[name] = units

        else:
            total_units[name] += units

    return total_units


# 9. Calculate total hours for each employee
def calculate_employee_hours(sales_data):

    total_hours = {}

    for sale in sales_data:

        name = sale["employee"]

        hours = sale["hours"]

        if name not in total_hours:
            total_hours[name] = hours

        else:
            total_hours[name] += hours

    return total_hours


# 10. Calculate average sale for each employee
def calculate_employee_average_sales(sales_data):

    total_sales = {}

    sale_count = {}

    for sale in sales_data:

        name = sale["employee"]

        sale_amount = sale["units"] * sale["unit_price"]

        if name not in total_sales:

            total_sales[name] = sale_amount

            sale_count[name] = 1

        else:

            total_sales[name] += sale_amount

            sale_count[name] += 1

    employee_average = {}

    for name in total_sales:

        employee_average[name] = total_sales[name] / sale_count[name]

    return employee_average


# 11. Calculate sales per hour for each employee
def calculate_employee_sales_per_hour(sales_data):

    employee_hours = calculate_employee_hours(sales_data)

    employee_sales = calculate_employee_sales(sales_data)

    sales_per_hour = {}

    for employee in employee_sales:

        sales = employee_sales[employee]

        hours = employee_hours[employee]

        sales_per_hour[employee] = sales / hours

    return sales_per_hour


# 12. Calculate target achievement for each employee
def calculate_employee_target_achievement(sales_data):

    employee_sales = calculate_employee_sales(sales_data)

    employee_targets = {}

    for sale in sales_data:

        name = sale["employee"]

        target = sale["target"]

        if name not in employee_targets:
            employee_targets[name] = target

        else:
            employee_targets[name] += target

    target_achievement = {}

    for employee in employee_sales:

        sales = employee_sales[employee]

        target = employee_targets[employee]

        target_achievement[employee] = (sales / target) * 100

    return target_achievement


# 13. Determine employee target performance
def determine_employee_target_performance(employee_target_achievement):

    employee_performance = {}

    for employee, achievement in employee_target_achievement.items():

        if achievement >= 120:

            employee_performance[employee] = "Outstanding"

        elif achievement >= 100:

            employee_performance[employee] = "Excellent"

        elif achievement >= 85:

            employee_performance[employee] = "Good"

        elif achievement >= 70:

            employee_performance[employee] = "Average"

        else:

            employee_performance[employee] = "Needs Improvement"

    return employee_performance


# 14. Determine employee hourly performance
def determine_employee_hourly_performance(employee_sales_per_hour):

    employee_performance = {}

    for employee, sales_per_hour in employee_sales_per_hour.items():

        if sales_per_hour >= 350:

            employee_performance[employee] = "Elite"

        elif sales_per_hour >= 250:

            employee_performance[employee] = "Excellent"

        elif sales_per_hour >= 200:

            employee_performance[employee] = "Good"

        else:

            employee_performance[employee] = "Needs Improvement"

    return employee_performance


# ============================================
# REPORT CREATION
# ============================================


def create_sales_report(sales_data):

    # Stage 1
    number_of_records = count_sales_records(sales_data)

    total_unit_sold = calculate_total_units(sales_data)

    total_sale = calculate_total_sales(sales_data)

    average = average_sales_revenue(total_sale, sales_data)

    highest_sale = find_highest_sales(sales_data)

    lowest_sale = find_lowest_sale(sales_data)

    # Stage 2
    employee_sales = calculate_employee_sales(sales_data)

    employee_units = calculate_employee_units(sales_data)

    employee_hours = calculate_employee_hours(sales_data)

    employee_average = calculate_employee_average_sales(sales_data)

    employee_sales_per_hour = calculate_employee_sales_per_hour(sales_data)

    employee_target_achievement = calculate_employee_target_achievement(sales_data)

    employee_target_performance = determine_employee_target_performance(
        employee_target_achievement
    )

    employee_hourly_performance = determine_employee_hourly_performance(
        employee_sales_per_hour
    )

    return {

        # Company
        "number_of_records": number_of_records,
        "total_unit_solds": total_unit_sold,
        "total_sales": total_sale,
        "average_sale": average,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,

        # Employee
        "employee_sales": employee_sales,
        "employee_units": employee_units,
        "employee_hours": employee_hours,
        "employee_average": employee_average,
        "employee_sales_per_hour": employee_sales_per_hour,
        "employee_target_achievement": employee_target_achievement,
        "employee_target_performance": employee_target_performance,
        "employee_hourly_performance": employee_hourly_performance
    }


# ============================================
# REPORT DISPLAY
# ============================================


def print_sales_report(report):

    print()

    print("=" * 110)

    print("                         SALES PERFORMANCE REPORT")

    print("=" * 110)

    # ----------------------------------------
    # COMPANY OVERVIEW
    # ----------------------------------------

    print()

    print("COMPANY OVERVIEW")

    print("-" * 110)

    print(f"Number of sales records : {report['number_of_records']}")

    print(f"Total units sold        : {report['total_unit_solds']}")

    print(f"Total sales revenue     : ${report['total_sales']:,.2f}")

    print(f"Average sale revenue    : ${report['average_sale']:,.2f}")

    print(f"Highest sale revenue    : ${report['highest_sale']:,.2f}")

    print(f"Lowest sale revenue     : ${report['lowest_sale']:,.2f}")


    # ----------------------------------------
    # EMPLOYEE PERFORMANCE
    # ----------------------------------------

    print()

    print("EMPLOYEE PERFORMANCE")

    print("-" * 110)

    print(
        f"{'Employee':<12}"
        f"{'Units':>8}"
        f"{'Hours':>9}"
        f"{'Avg Sale':>15}"
        f"{'Total Sales':>17}"
        f"{'Sales/Hour':>15}"
        f"{'Target %':>12}"
    )

    print("-" * 110)

    for employee in report["employee_sales"]:

        sales = report["employee_sales"][employee]

        units = report["employee_units"][employee]

        hours = report["employee_hours"][employee]

        average = report["employee_average"][employee]

        sales_per_hour = report["employee_sales_per_hour"][employee]

        target_achievement = report["employee_target_achievement"][employee]

        print(
            f"{employee:<12}"
            f"{units:>8}"
            f"{hours:>9}$"
            f"{average:>14,.2f}$"
            f"{sales:>16,.2f}"
            f"{sales_per_hour:>14,.2f}"
            f"{target_achievement:>11.2f}%"
        )

    print()

    print("=" * 110)

    print("                              END OF REPORT")

    print("=" * 110)


# ============================================
# MAIN PROGRAM
# ============================================


report = create_sales_report(sales_data)

print_sales_report(report)