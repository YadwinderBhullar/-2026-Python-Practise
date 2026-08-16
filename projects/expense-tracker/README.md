# Expense Tracker

## Overview

Expense Tracker is a Python project that analyzes personal expense data and generates a detailed financial report.

The project was built to practice Python fundamentals through a realistic data-analysis problem using lists, dictionaries, loops, functions, conditions, calculations, and dictionary-based aggregation.

## Features

The program currently calculates:

* Total expenses
* Average expense
* Highest expense
* Lowest expense
* Total spending by category
* Number of transactions in each category
* Average expense by category
* Spending percentage by category
* Highest spending category
* Highest spending percentage
* Highest average expense category
* Monthly budget
* Remaining budget
* Budget usage percentage
* Budget status
* Number of expense records
* Complete expense report

## Example Data

```python
expenses = [
    {"category": "Food", "amount": 45},
    {"category": "Transport", "amount": 20},
    {"category": "Food", "amount": 30},
    {"category": "Entertainment", "amount": 60},
    {"category": "Transport", "amount": 15},
    {"category": "Bills", "amount": 100}
]

monthly_budget = 300
```

## Example Results

### Overall Expenses

```text
Number of expenses: 6
Total expenses: $270
Average expense: $45
Highest expense: $100
Lowest expense: $15
```

### Category Analysis

```text
Food
  Total: $75
  Transactions: 2
  Average: $37.50
  Percentage: 27.78%

Transport
  Total: $35
  Transactions: 2
  Average: $17.50
  Percentage: 12.96%

Entertainment
  Total: $60
  Transactions: 1
  Average: $60.00
  Percentage: 22.22%

Bills
  Total: $100
  Transactions: 1
  Average: $100.00
  Percentage: 37.04%
```

### Budget Analysis

```text
Monthly budget: $300
Total spent: $270
Remaining budget: $30
Budget used: 90%
Status: Within Budget
```

### Highlights

```text
Highest spending category: Bills
Highest spending percentage: Bills
Highest average expense category: Bills
```

## Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
└── README.md
```

## Functions

The project is organized into separate functions for each analysis task, including:

```python
calculate_total_expenses()
calculate_average_expense()
calculate_highest_expense()
calculate_lowest_expense()
calculate_category_totals()
count_expenses_by_category()
calculate_average_by_category()
highest_spending_category()
spending_percentage_by_category()
find_highest_spending_percentage()
calculate_budget_status()
check_budget_status()
count_expenses()
calculate_highest_average_category()
create_expense_report()
print_expense_report()
```

## Skills Practiced

This project demonstrates practice with:

* Python lists
* Dictionaries
* Nested dictionaries
* `for` loops
* `if/elif/else`
* Functions
* Function parameters
* Return values
* Tuple unpacking
* Dictionary `.items()` and `.values()`
* Counters and accumulators
* Finding highest and lowest values
* Basic financial calculations
* Grouping data by category
* Calculating percentages
* Building summary reports
* Git and GitHub

## Development Tasks

* [x] Create expense data
* [x] Calculate total expenses
* [x] Calculate average expense
* [x] Find highest expense
* [x] Find lowest expense
* [x] Calculate category totals
* [x] Create final expense report
* [x] Find highest spending category
* [x] Calculate spending percentage by category
* [x] Find highest spending percentage
* [x] Add monthly budget
* [x] Calculate remaining budget
* [x] Calculate budget usage percentage
* [x] Check budget status
* [x] Count total expenses
* [x] Count expenses by category
* [x] Calculate average expense by category
* [x] Find highest average expense category
* [x] Build complete final report
* [x] Test the project with sample data

## How to Run

Make sure Python is installed.

From the project directory, run:

```bash
python expense_tracker.py
```

The program will calculate the expense statistics and display the complete report in the terminal.

## Future Improvements

Possible future improvements include:

* Allow users to enter expenses interactively
* Add dates to each expense
* Analyze expenses by month
* Save expense data to a CSV file
* Read expense data from CSV
* Use Pandas for data analysis
* Add charts and visualizations
* Add automated unit tests
* Add input validation
* Build a graphical or web interface

## Project Status

**Completed — Version 1**

This project is a Python learning and portfolio project focused on building a small data-analysis application from the ground up.
