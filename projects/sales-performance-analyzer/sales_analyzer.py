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

# 2. Calucalte total unit sold
def calculate_total_units(sales_data):
    total_units = 0
    for sale in sales_data:
        total_units += sale["units"]
    return total_units


# 3. Calculate total sales reveneue

def calculate_total_sales(sales_data):
    total_sales = 0 
    for sale in sales_data:
        total_sale = sale["units"] * sale["unit_price"]
        total_sales += total_sale
       
    return total_sales

# 4 Calculate average sales revenue

def average_sales_revenue(total_sales, sales_data):

    average = total_sales / len(sales_data)

    return average


# 5 Find the highest sales revenue

def find_highest_sales(sales_data):
    highest_sale = 0
    for sale in sales_data:
        total_sale = sale["units"] * sale["unit_price"]
        if total_sale > highest_sale:
            highest_sale = total_sale
    return highest_sale

# 6 Find lowest sales by revenue

def find_lowest_sale(sales_data):
    lowest_sale = 999
    for sale in sales_data:
        total_sale = sale["units"] * sale["unit_price"]
        if total_sale <lowest_sale:
            lowest_sale = total_sale
    return lowest_sale
# ============================================
# Employee analaysis 
# ============================================

# 7 Calculate each employee sales
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



#8 calculate how many units each employee sold
def calculate_employee_units(sales_data):
    total_units = {}
    for sale in sales_data:
        name = sale["employee"]
        total_unit = sale["units"]
        if name not in total_units:
            total_units[name] = total_unit
        else: 
            total_units[name] += total_unit
    return total_units
# Calculate employee hours 

def calculate_employee_hours(sales_data):
    total_hours= {

    }
    for sale in sales_data:
        name= sale["employee"]
        hours=sale["hours"]
        if name not in total_hours:
            total_hours[name]= hours
        else :
            total_hours[name]+= hours
    return total_hours






# ============================================
# REPORT CREATION
# ============================================
def create_sales_report(sales_data):

    number_of_records = count_sales_records(sales_data)
    total_unit_sold = calculate_total_units(sales_data)
    total_sale = calculate_total_sales(sales_data)
    average = average_sales_revenue(total_sale, sales_data)
    highest_sale = find_highest_sales(sales_data)
    lowest_sale = find_lowest_sale(sales_data)

    employee_sales = calculate_employee_sales(sales_data)
    employee_units = calculate_employee_units(sales_data)
    employee_hours = calculate_employee_hours(sales_data)

    return {
        "number_of_records": number_of_records,
        "total_unit_solds": total_unit_sold,
        "total_sales": total_sale,
        "average_sale": average,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,
        "employee_sales": employee_sales,
        "employee_units": employee_units,
        "employee_hours": employee_hours
    }



# ============================================
# REPORT DISPLAY
# ============================================

def print_sales_report(report):

    print()
    print("=" * 65)
    print("                 SALES PERFORMANCE REPORT")
    print("=" * 65)

    print()
    print("COMPANY OVERVIEW")
    print("-" * 65)

    print(f"Number of sales records : {report['number_of_records']}")
    print(f"Total units sold       : {report['total_unit_solds']}")
    print(f"Total sales revenue    : ${report['total_sales']:,.2f}")
    print(f"Average sale revenue   : ${report['average_sale']:,.2f}")
    print(f"Highest sale revenue   : ${report['highest_sale']:,.2f}")
    print(f"Lowest sale revenue    : ${report['lowest_sale']:,.2f}")

    print("EMPLOYEE PERFORMANCE")
    print("-" * 65)
    print(f"{'Employee':<15}{'Units Sold':>12}{'Hours':>12}{'Total Sales':>20}")
    print("-" * 65)

    for employee in report["employee_sales"]:

        sales = report["employee_sales"][employee]
        units = report["employee_units"][employee]
        hours = report["employee_hours"][employee]

        sales_display = f"{sales:,.2f}$"

        print(
            f"{employee:<15}"
            f"{units:>12}"
            f"{hours:>12}"
            f"{sales_display:>20}"
)
    print()
    print("=" * 65)
    print("                    END OF REPORT")
    print("=" * 65)

# ============================================
# MAIN PROGRAM
# ============================================

report = create_sales_report(sales_data)

print_sales_report(report)