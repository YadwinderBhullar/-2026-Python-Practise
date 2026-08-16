# ============================================
# EXPENSE TRACKER
# ============================================

expenses = [
    {"category": "Food", "amount": 45},
    {"category": "Transport", "amount": 20},
    {"category": "Food", "amount": 30},
    {"category": "Entertainment", "amount": 60},
    {"category": "Transport", "amount": 15},
    {"category": "Bills", "amount": 100}
]

monthly_budget = 300


# ============================================
# 1. Calculate total expenses
# ============================================

def calculate_total_expenses(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# ============================================
# 2. Calculate average expense
# ============================================

def calculate_average_expense(expenses):

    total = calculate_total_expenses(expenses)

    average = total / len(expenses)

    return average


# ============================================
# 3. Find highest expense
# ============================================

def calculate_highest_expense(expenses):

    highest = 0

    for expense in expenses:

        if expense["amount"] > highest:
            highest = expense["amount"]

    return highest


# ============================================
# 4. Find lowest expense
# ============================================

def calculate_lowest_expense(expenses):

    lowest = 999999

    for expense in expenses:

        if expense["amount"] < lowest:
            lowest = expense["amount"]

    return lowest


# ============================================
# 5. Calculate category totals
# ============================================

def calculate_category_totals(expenses):

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals


# ============================================
# 6. Count expenses by category
# ============================================

def count_expenses_by_category(expenses):

    category_counts = {}

    for expense in expenses:

        category = expense["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    return category_counts


# ============================================
# 7. Calculate average expense by category
# ============================================

def calculate_average_by_category(category_totals, category_counts):

    category_averages = {}

    for category in category_totals:

        total = category_totals[category]
        count = category_counts[category]

        average = total / count

        category_averages[category] = average

    return category_averages


# ============================================
# 8. Find highest spending category
# ============================================

def highest_spending_category(category_totals):

    highest_amount = 0
    highest_category = ""

    for category, amount in category_totals.items():

        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    return highest_category, highest_amount


# ============================================
# 9. Calculate spending percentage by category
# ============================================

def spending_percentage_by_category(category_totals, total_expenses):

    category_percentages = {}

    for category, amount in category_totals.items():

        percentage = (amount / total_expenses) * 100

        category_percentages[category] = percentage

    return category_percentages


# ============================================
# 10. Find highest spending percentage
# ============================================

def find_highest_spending_percentage(percentages):

    highest_percentage = 0
    highest_category = ""

    for category, percentage in percentages.items():

        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_category = category

    return highest_category, highest_percentage


# ============================================
# 11. Calculate budget status
# ============================================

def calculate_budget_status(total_expenses, monthly_budget):

    remaining_budget = monthly_budget - total_expenses

    budget_used = (total_expenses / monthly_budget) * 100

    return remaining_budget, budget_used


# ============================================
# 12. Check budget status
# ============================================

def check_budget_status(total_expenses, monthly_budget):

    if total_expenses <= monthly_budget:
        return "Within Budget"
    else:
        return "Over Budget"


# ============================================
# 13. Count total number of expenses
# ============================================

def count_expenses(expenses):

    count = 0

    for expense in expenses:
        count += 1

    return count


# ============================================
# 14. Find highest average expense category
# ============================================

def calculate_highest_average_category(category_averages):

    highest_average = 0
    highest_category = ""

    for category, average in category_averages.items():

        if average > highest_average:
            highest_average = average
            highest_category = category

    return highest_category, highest_average


# ============================================
# 15. Create complete expense report
# ============================================

def create_expense_report(expenses, monthly_budget):

    total_expenses = calculate_total_expenses(expenses)

    average_expense = calculate_average_expense(expenses)

    highest_expense = calculate_highest_expense(expenses)

    lowest_expense = calculate_lowest_expense(expenses)

    number_of_expenses = count_expenses(expenses)

    category_totals = calculate_category_totals(expenses)

    category_counts = count_expenses_by_category(expenses)

    category_averages = calculate_average_by_category(
        category_totals,
        category_counts
    )

    category_percentages = spending_percentage_by_category(
        category_totals,
        total_expenses
    )

    highest_category, highest_category_amount = (
        highest_spending_category(category_totals)
    )

    highest_percentage_category, highest_percentage = (
        find_highest_spending_percentage(category_percentages)
    )

    highest_average_category, highest_average = (
        calculate_highest_average_category(category_averages)
    )

    remaining_budget, budget_used = calculate_budget_status(
        total_expenses,
        monthly_budget
    )

    budget_status = check_budget_status(
        total_expenses,
        monthly_budget
    )

    return {
        "number_of_expenses": number_of_expenses,
        "total_expenses": total_expenses,
        "average_expense": average_expense,
        "highest_expense": highest_expense,
        "lowest_expense": lowest_expense,
        "category_totals": category_totals,
        "category_counts": category_counts,
        "category_averages": category_averages,
        "category_percentages": category_percentages,
        "highest_category": highest_category,
        "highest_category_amount": highest_category_amount,
        "highest_percentage_category": highest_percentage_category,
        "highest_percentage": highest_percentage,
        "highest_average_category": highest_average_category,
        "highest_average": highest_average,
        "monthly_budget": monthly_budget,
        "remaining_budget": remaining_budget,
        "budget_used": budget_used,
        "budget_status": budget_status
    }


# ============================================
# 16. Print complete expense report
# ============================================

def print_expense_report(report):

    print()
    print("============================================")
    print("            EXPENSE TRACKER REPORT")
    print("============================================")
    print()

    # Overall statistics
    print("---------- OVERALL EXPENSES ----------")
    print()

    print(
        "Number of expenses:",
        report["number_of_expenses"]
    )

    print(
        "Total expenses: $",
        round(report["total_expenses"], 2)
    )

    print(
        "Average expense: $",
        round(report["average_expense"], 2)
    )

    print(
        "Highest expense: $",
        round(report["highest_expense"], 2)
    )

    print(
        "Lowest expense: $",
        round(report["lowest_expense"], 2)
    )

    # Category summary
    print()
    print("---------- CATEGORY SUMMARY ----------")
    print()

    for category in report["category_totals"]:

        total = report["category_totals"][category]
        count = report["category_counts"][category]
        average = report["category_averages"][category]
        percentage = report["category_percentages"][category]

        print(category)
        print("  Total: $", round(total, 2))
        print("  Transactions:", count)
        print("  Average: $", round(average, 2))
        print("  Percentage:", round(percentage, 2), "%")
        print()

    # Budget
    print("---------- BUDGET ----------")
    print()

    print(
        "Monthly budget: $",
        round(report["monthly_budget"], 2)
    )

    print(
        "Total spent: $",
        round(report["total_expenses"], 2)
    )

    print(
        "Remaining budget: $",
        round(report["remaining_budget"], 2)
    )

    print(
        "Budget used:",
        round(report["budget_used"], 2),
        "%"
    )

    print(
        "Status:",
        report["budget_status"]
    )

    # Highlights
    print()
    print("---------- HIGHLIGHTS ----------")
    print()

    print(
        "Highest spending category:",
        report["highest_category"],
        "- $",
        round(report["highest_category_amount"], 2)
    )

    print(
        "Highest spending percentage:",
        report["highest_percentage_category"],
        "-",
        round(report["highest_percentage"], 2),
        "%"
    )

    print(
        "Highest average expense category:",
        report["highest_average_category"],
        "- $",
        round(report["highest_average"], 2)
    )

    print()


# ============================================
# MAIN PROGRAM
# ============================================

report = create_expense_report(
    expenses,
    monthly_budget
)

print_expense_report(report)