# write a code for Takes a list of numbers and counts how many numbers are greater than 10. and numbers=[5,12,8,20,15,3]

def count_greater_than_10(numbers):
    count=0
    for num in numbers:
        if num >10:
            count+=1
    return count

result =count_greater_than_10([5,12,8,20,15,3])

print(result)
