# Employee Data Analysis

## Overview

The Employee Data Analysis project is a Python application that analyzes employee sales performance, productivity, bonuses, and department-level results.

The project focuses on applying reusable functions and structured data to solve a more realistic business-analysis problem.

## Features

* Calculates total sales for each employee
* Calculates sales per hour
* Determines employee performance level
* Calculates performance-based bonuses
* Identifies the top performer
* Identifies the lowest performer
* Calculates total company sales
* Calculates total company bonuses
* Groups sales by department
* Calculates average sales per department employee
* Identifies the best-performing department
* Counts employees rated Excellent

## Performance Rules

| Sales Per Hour | Performance       |
| -------------: | ----------------- |
|    300 or more | Excellent         |
|     250–299.99 | Good              |
|     200–249.99 | Average           |
|      Below 200 | Needs Improvement |

## Bonus Rules

| Performance       |              Bonus |
| ----------------- | -----------------: |
| Excellent         | 15% of total sales |
| Good              | 10% of total sales |
| Average           |  5% of total sales |
| Needs Improvement |                 0% |

## Example Results

```text
========== COMPANY SUMMARY ==========

Total company sales: $172500
Total company bonus: $16725

Top performer: Sarah
Top sales per hour: $334.29

Lowest performer: Mike
Lowest sales per hour: $206.67

Excellent employees: 1
```

## Department Results

```text
Sales
Total Sales: $96500
Average/Employee: $48250

Marketing
Total Sales: $76000
Average/Employee: $38000

Best department by total sales: Sales
Best department by average sales: Sales
```

## Technologies

* Python
* Dictionaries
* Lists
* Loops
* Conditional logic
* Functions
* Return values
* Dictionary aggregation
* Basic business data analysis

## Key Learning Outcomes

This project demonstrates how to build a multi-function Python application where individual functions perform specific responsibilities and work together to generate a larger analysis.

It also demonstrates grouping and aggregating business data by department, finding maximum and minimum values, counting matching records, and calculating derived business metrics.

## Future Improvements

* Replace hard-coded data with CSV or Excel input
* Use Pandas for larger datasets
* Add data validation
* Add automated unit tests
* Export reports to CSV
* Create charts for sales and productivity
* Build a simple dashboard
* Add SQL database integration
