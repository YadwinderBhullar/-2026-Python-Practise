sales = {
    "Alex": [1200, 800, 1500],
    "Sarah": [900, 1100, 700],
    "Yadwinder": [2000, 1800, 2200],
    "Mike": [600, 750, 500]
}
# caluclate each enmployee's total sales
# Determine there performance Total >= 5000 → "Excellent" Total >= 3000 → "Good"Otherwise → "Needs Improvement" 3. Find the employee with the highest total sales.

#Expected:

#Top salesperson: Yadwinder
#Top sales: 6000 4. Count how many employees achieved "Good" or "Excellent" performance. Expected: Employees meeting target: 2
top_saleperson=""
top_sales=0
count=0
for name, values in sales.items():
    total_sales=0

    for value in values:
        total_sales= total_sales + value

    if total_sales>=5000:
     print(name,"Excellent")

     count=count+1
    elif total_sales >=3000:
     print( name, "Good")
     count=count+1

    else:
     print(name, "Need Improvement")

    if total_sales> top_sales:
      top_sales=total_sales
      top_saleperson =name

    print(name,total_sales)
    print("Top sales person is :", top_saleperson)
    print("Top sales is :", top_sales)
    print("Total number of employes that are Excellent", count)