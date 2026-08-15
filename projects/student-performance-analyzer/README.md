# Student Performance Analyzer

## Overview

The Student Performance Analyzer is a Python application that evaluates student grades and produces a simple class performance report.

The project was built to practice Python fundamentals such as functions, dictionaries, lists, loops, conditional statements, function calls, and return values.

## Features

* Calculates each student's average mark
* Determines PASS or FAIL status
* Finds the student with the highest average
* Finds the student with the lowest average
* Generates a class summary
* Uses reusable functions instead of repeating calculations

## Example Data

```python
students = {
    "John": [78, 85, 92],
    "Mike": [45, 55, 60],
    "Sarah": [90, 95, 88],
    "David": [35, 42, 48]
}
```

## Example Output

```text
========== STUDENT REPORT ==========

Student: John
Marks: [78, 85, 92]
Average: 85.0
Result: PASS

Student: Mike
Marks: [45, 55, 60]
Average: 53.33
Result: PASS

Student: Sarah
Marks: [90, 95, 88]
Average: 91.0
Result: PASS

Student: David
Marks: [35, 42, 48]
Average: 41.67
Result: FAIL

========== CLASS SUMMARY ==========

Highest average: Sarah - 91.0
Lowest average: David - 41.67
```

## Technologies

* Python
* Lists
* Dictionaries
* `for` loops
* `if / else`
* Functions
* Return values
* Basic data analysis

## Key Learning Outcomes

This project demonstrates the ability to break a larger problem into reusable functions and pass data between functions.

It also demonstrates how to iterate through structured data and maintain values such as the highest and lowest results.

## Future Improvements

* Add interactive user input
* Calculate median and class statistics
* Add subject names
* Export reports to CSV
* Add automated tests
* Build a Pandas version
