employees = {
    "John": {
        "sales": [12000, 15000, 11000],
        "hours": 160
    },

    "Sarah": {
        "sales": [18000, 21000, 19500],
        "hours": 175
    },

    "Mike": {
        "sales": [9000, 12000, 10000],
        "hours": 150
    },

    "David": {
        "sales": [15000, 14000, 16000],
        "hours": 165
    }
}
def calculate_total_sales(sales):
    total=0
    for sale in sales:
        total=sale +total

    return total

def calculate_sales_per_hour(sales,hours):
   
    total = calculate_total_sales(sales)

    sales_per_hour =total /hours

    return sales_per_hour

 


def analyze_employe(name,data):
    sales = data["sales"]
    hours = data["hours"]

    total_sales =calculate_total_sales(sales)
    sales_per_hour = calculate_sales_per_hour(sales,hours)

    return total_sales,sales_per_hour



def determine_performance(sales_per_hour):
    if sales_per_hour>= 300:
        return "Excellent"
    elif sales_per_hour>=250:
        return "Good"
    elif sales_per_hour>= 200:
        return "Average"

    else: 
        return "Needs Improvement"



def calculate_bonus(total_sales, performance):

    if performance == "Excellent":
        return total_sales * 0.15

    elif performance == "Good":
        return total_sales * 0.10

    elif performance == "Average":
        return total_sales * 0.05

    else:
        return 0

def calculate_top_performer(employees):
    highest_sales_per_hour =0
    top_employee =""

    for name, data in  employees.items():
        total, sales_per_hour = analyze_employe(name, data)
        if sales_per_hour> highest_sales_per_hour:
           highest_sales_per_hour= sales_per_hour
           top_employee =name

    return highest_sales_per_hour,top_employee

top_rate, top_performer = calculate_top_performer(employees)
print("Top Performer: ", top_performer)
print("Sales per hour:", round(top_rate, 2))
print()

def calculate_lowest_performer(employees):
    lowest_sales_per_hour =999
    lowest_employee =""
    
    for name, data in  employees.items():
        total, sales_per_hour = analyze_employe(name, data)
        if sales_per_hour <lowest_sales_per_hour:
               lowest_sales_per_hour = sales_per_hour
               lowest_employee = name

    
    return lowest_sales_per_hour,lowest_employee
    
lowest_rate, lowest_employee = calculate_lowest_performer(employees)
print("Lowest Performer: ", lowest_employee)
print("Sales per hour:", round(lowest_rate, 2))
print()

def calculate_company_summary(employees):
    total_sales=0
    total_bonus=0
    for name, data in employees.items():
        total,sales_per_hour = analyze_employe(name,data)
        performance =determine_performance(sales_per_hour)

        bonus =calculate_bonus(total,performance)

       
        total_sales = sales_per_hour + total
        total_bonus= bonus + total_bonus

    return total_sales, total_bonus
company_sales ,company_bonus= calculate_company_summary(employees)

print("Total company sales:", company_sales)
print("Total company bonus:", company_bonus)


for name, data in employees.items():

    total, rate = analyze_employe(name, data)

    performance = determine_performance(rate)

    bonus = calculate_bonus(total, performance)
   

    print("Employee:", name)
    print("Total sales:", total)
    print("Sales per hour:", round(rate, 2))
    print("Performance:", performance)
    print("Bonus:", round(bonus, 2))
    print()