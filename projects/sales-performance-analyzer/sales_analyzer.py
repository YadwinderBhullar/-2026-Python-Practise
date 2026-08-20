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

# 1. Count number of sales records
def count_sales_records(sales_data):

    count = 0

    for sale in sales_data:
        count += 1

    return count

# 2. Calucalte total unit sold
def calculate_total_unit_sold(sales_data):
    total_units = 0
    for sale in sales_data:
        total_units += sale["units"]
    return total_units


# 3. Calculate total sales reveneue

def calculate_total_sales_revenue(sales_data):
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

def calcualte_highest_sales(sales_data):
    highest_sale = 0
    for sale in sales_data:
        total_sale = sale["units"] * sale["unit_price"]
        if total_sale > highest_sale:
            highest_sale = total_sale
    return highest_sale








# ============================================
# REPORT CREATION
# ============================================
def create_sales_report(sales_data):

    number_of_records = count_sales_records(sales_data)
    total_unit_sold = calculate_total_unit_sold(sales_data)
    total_sale = calculate_total_sales_revenue(sales_data)
    average = average_sales_revenue(total_sale, sales_data)
    highest_sale = calcualte_highest_sales(sales_data)


    return {
        "number_of_records": number_of_records,
        "total_unit_solds": total_unit_sold,
        "total_sales": total_sale,
        "average_sale": average,
        "highest_sale": highest_sale
    }


# ============================================
# REPORT DISPLAY
# ============================================

def print_sales_report(report):

    print()
    print("========== SALES PERFORMANCE REPORT ==========")
    print()

    print("Number of sales records:", report["number_of_records"])
    print("total unit sold", report["total_unit_solds"])
    print("total sale of revenue is : ", report["total_sales"])
    print("Average sale revenue: $", (round(report["average_sale"] ,2)))
    print("Highest sale revenue: $", report["highest_sale"])


# ============================================
# MAIN PROGRAM
# ============================================

report = create_sales_report(sales_data)

print_sales_report(report)