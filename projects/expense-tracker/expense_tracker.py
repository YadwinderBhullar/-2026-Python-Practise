



# 6. Generate final expense report


expenses = [
    {"category": "Food", "amount": 45},
    {"category": "Transport", "amount": 20},
    {"category": "Food", "amount": 30},
    {"category": "Entertainment", "amount": 60},
    {"category": "Transport", "amount": 15},
    {"category": "Bills", "amount": 100}
]

# 1. Calculate total expenses
def calculate_total_expenses(expenses):

    total=0

    for expense in expenses:
        total += expense["amount"]

    return total

print(calculate_total_expenses(expenses))

# 2. Calculate average expense
def calculate_average_expense(expenses):

    total = calculate_total_expenses(expenses)

    average = total / len(expenses)

    return average
print(calculate_average_expense(expenses))


# 3. Find highest expense
def calculate_highest_expense(expenses):

    highest = 0

    for expense in expenses:

        if expense["amount"] > highest:
            highest = expense["amount"]
    return highest
print(calculate_highest_expense(expenses))

# 4. Find lowest expense
def calculate_lowest_expense(expenses):

    lowest = 999

    for expense in expenses:

        if expense["amount"] < lowest :
            lowest = expense["amount"]
    return lowest
print(calculate_lowest_expense(expenses))

# 5. Calculate category totals
def calculate_category_totals(expenses):

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals


category_totals = calculate_category_totals(expenses)

print(category_totals)



