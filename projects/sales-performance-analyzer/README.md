# Advanced Sales Performance Analyzer

## Overview

Advanced Sales Performance Analyzer is a Python project designed to analyze sales, employee performance, departments, regions, products, and sales targets.

This project is being built progressively from basic Python concepts toward more advanced data-analysis and problem-solving techniques.

The project uses a list of dictionaries as its main dataset and gradually combines multiple calculations and aggregations into a complete sales performance report.

## Project Goals

The program will eventually analyze:

* Sales records
* Employees
* Departments
* Regions
* Products
* Units sold
* Sales revenue
* Working hours
* Sales targets
* Target achievement
* Employee performance

## Dataset Structure

Each sales record contains:

```python
{
    "employee": "John",
    "department": "Electronics",
    "region": "East",
    "product": "Laptop",
    "units": 8,
    "unit_price": 1200,
    "hours": 40,
    "target": 9000
}
```

Each record contains:

* `employee`
* `department`
* `region`
* `product`
* `units`
* `unit_price`
* `hours`
* `target`

The same employee can appear in multiple records. This requires the program to combine and aggregate data rather than simply analyze individual records.

## Analysis Planned

### Company Analysis

The program will calculate:

* Number of sales records
* Number of employees
* Number of departments
* Number of regions
* Number of products
* Total sales
* Total units sold
* Average sale
* Highest sale
* Lowest sale

### Employee Analysis

For each employee:

* Total sales
* Total units sold
* Average sale
* Sales per hour
* Sales target
* Target achievement percentage
* Target performance
* Hourly performance

### Department Analysis

For each department:

* Number of employees
* Total sales
* Total units
* Average sales per employee
* Percentage of company sales
* Target performance

### Regional Analysis

For each region:

* Total sales
* Total units
* Average sales
* Top employee
* Percentage of company sales

### Product Analysis

For each product:

* Units sold
* Revenue
* Average selling price
* Top-selling product

### Target Analysis

The program will identify:

* Employees above target
* Employees below target
* Overall target achievement
* Highest target achievement
* Lowest target achievement

## Performance Rules

### Target Achievement

```text
120% or higher → Outstanding
100% or higher → Excellent
85% or higher  → Good
70% or higher  → Average
Below 70%      → Needs Improvement
```

### Sales Per Hour

```text
350 or higher → Elite
250 or higher → Excellent
200 or higher → Good
Below 200     → Needs Improvement
```

## Python Concepts Practiced

This project will use and strengthen:

* Variables
* Strings
* Integers and floats
* Lists
* Dictionaries
* Lists of dictionaries
* `for` loops
* `if`, `elif`, and `else`
* Functions
* Parameters and arguments
* Return values
* Multiple return values
* Tuple unpacking
* Counters
* Accumulators
* Dictionary aggregation
* `.items()`
* `.keys()`
* `.values()`
* Highest and lowest value logic
* Averages
* Percentages
* Data grouping
* Nested calculations
* Report generation

## Development Approach

The project will be developed gradually.

Each feature will be:

1. Implemented as a function.
2. Tested independently.
3. Added to the final report.
4. Added to the print report.
5. Committed to Git.

The final report will grow alongside the project instead of being built all at once.

## Development Stages

### Stage 1 — Basic Calculations

* Count sales records
* Calculate total units
* Calculate total sales
* Calculate average sales
* Find highest sale
* Find lowest sale

### Stage 2 — Employee Analysis

* Group sales by employee
* Calculate employee sales
* Calculate sales per hour
* Calculate target achievement
* Determine employee performance

### Stage 3 — Department Analysis

* Group employees by department
* Calculate department sales
* Calculate department units
* Calculate department averages
* Calculate department percentages

### Stage 4 — Region and Product Analysis

* Group sales by region
* Group sales by product
* Calculate regional performance
* Calculate product revenue
* Identify top products and regions

### Stage 5 — Final Report

Create a complete report containing company, employee, department, regional, product, and target analysis.

## Project Structure

```text
advanced-sales-analyzer/
│
├── sales_analyzer.py
└── README.md
```

## Git Development

The project will be developed through approximately 4–5 meaningful commits.

Example:

```text
Initialize advanced sales analyzer
Add basic sales calculations
Add employee performance analysis
Add department and regional analysis
Complete sales performance report
```

The commit history is intended to show the progression from basic Python logic to a more complete data-analysis application.

## Current Progress

### Stage 1

* [ ] Count sales records
* [ ] Calculate total units
* [ ] Calculate total sales
* [ ] Calculate average sales
* [ ] Find highest sale
* [ ] Find lowest sale

### Stage 2

* [ ] Employee sales
* [ ] Employee units
* [ ] Sales per hour
* [ ] Target achievement
* [ ] Employee performance

### Stage 3

* [ ] Department sales
* [ ] Department units
* [ ] Department averages
* [ ] Department percentages

### Stage 4

* [ ] Regional analysis
* [ ] Product analysis
* [ ] Top region
* [ ] Top product

### Stage 5

* [ ] Complete final report
* [ ] Testing
* [ ] Validation
* [ ] Final documentation

## Future Improvements

Possible future improvements include:

* CSV file input
* Data validation
* User input
* Date-based sales analysis
* Monthly reports
* Charts and visualizations
* Pandas implementation
* Automated tests
* Error handling
* Exporting reports to CSV or Excel

## Project Status

**In Progress**

This project is being developed as part of a Python learning and interview-preparation journey, with the goal of progressing from fundamental Python programming toward practical data analysis and more advanced problem solving.
