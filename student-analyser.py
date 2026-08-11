students = {
    "Alex": [85, 72, 91],
    "Sarah": [91, 45, 88],
    "Yadwinder": [95, 76, 99],
    "Mike": [55, 60, 90]
}
passed = 0
highest_average=0
top_student=""
for name, scores in students.items():
    total = 0
   
    for score in scores:
        total = total + score

    average = total / len(scores)

    print(name, "average:", average)



    if average >=70:
        print(name,"has passsed the classes")
        passed= passed +1
    else:
        print(name,"not passed the classes")
    if average>highest_average:
        highest_average = average
        top_student = name 

print()
print("top student",top_student)
print("Passed student", passed)
print("Top Average:", round(average,2))
   

