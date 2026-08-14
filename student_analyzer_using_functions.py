#
#We're going to build this step-by-step.

#Our program will eventually do 5 things:
#Find the total of all marks
#Find the average
#Count how many students passed
#Find the highest mark
#Find the lowest mark


def calculate_total (numbers):
    total=0

  
    for num in numbers:
       
            total = num + total
    return total
result= calculate_total([78, 45, 92, 66, 35, 88, 54, 71])


def average(numbers):
    total=0
    for num in numbers:
            total = num +  total
            average = total /len(numbers)
    return average
average_of_numbers = average([78, 45, 92, 66, 35, 88, 54, 71])

def count_passed_students(numbers):
    count=0
    
    for num in numbers:
            if num  >45:
               
                count +=1
    return count
total_passed_studnets= count_passed_students([78, 45, 92, 66, 35, 88, 54, 71])

def highest_marks(numbers):
    highest=numbers[0]
    for num in numbers:
        if num>highest:
          highest = num
    return highest
highest_numbers=highest_marks([78, 45, 92, 66, 35, 88, 54, 71])

def lowest_marks(numbers):
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
              lowest = num
    return lowest

lowest_number= lowest_marks([78, 45, 92, 66, 35, 88, 54, 71])

print("lowest marks is :", lowest_number)
     
print("Highest mark is :",highest_numbers)
                

print("Total number of students passed is ",total_passed_studnets)
print("Average of number is : ", average_of_numbers)
print("total is ",result)


