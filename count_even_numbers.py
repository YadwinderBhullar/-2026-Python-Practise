# cWrite a function that receives a list and returns:

#The number of even numbers AND the number of odd numbers.


def count_even_numbers(numbers):

    count = 0

    for num in numbers:
        if num %2 ==0:
            count+=1
    return count
result = count_even_numbers([2, 7, 4, 9, 10, 3])
print(result)