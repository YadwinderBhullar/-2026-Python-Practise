# Expense Tracker

## Overview

The Expense Tracker is a Python project that analyzes a collection of personal expenses and generates a summary report.

This project is designed to practice Python fundamentals by solving a realistic data-analysis problem using lists, dictionaries, loops, functions, conditions, and return values.

## Project Goals

The program will analyze expense data and calculate:

* Total expenses
* Average expense
* Highest expense
* Lowest expense
* Total spending by category

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
```

## Expected Results

### Overall Statistics

```text
Total expenses: $270
Average expense: $45.00
Highest expense: $100
Lowest expense: $15
```

### Category Totals

```text
Food: $75
Transport: $35
Entertainment: $60
Bills: $100
```

## Planned Functions

The project will be developed using separate functions:

```python
def calculate_total_expenses(expenses):
    pass

def calculate_average_expense(expenses):
    pass

def find_highest_expense(expenses):
    pass

def find_lowest_expense(expenses):
    pass

def calculate_category_totals(expenses):
    pass
```

## Development Tasks

* [ ] Create the expense data
* [ ] Calculate total expenses
* [ ] Calculate average expense
* [ ] Find highest expense
* [ ] Find lowest expense
* [ ] Calculate category totals
* [ ] Build the final expense report
* [ ] Test the program with the sample data
* [ ] Add input validation
* [ ] Add automated tests
* [ ] Improve documentation

## Skills Practiced

* Python lists
* Python dictionaries
* Nested dictionaries
* `for` loops
* Conditional statements
* Functions
* Function parameters
* Return values
* Dictionary aggregation
* Basic data analysis
* Git and GitHub

## Future Improvements

Possible future improvements include:

* Allow users to enter expenses
* Add dates to expenses
* Analyze monthly spending
* Calculate spending percentages by category
* Export the results to CSV
* Build a Pandas version
* Add charts and data visualization
* Add automated unit tests

## Project Status

**In Development**

The project is being built incrementally, with each feature implemented and tested separately.
