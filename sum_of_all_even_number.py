# crate a code to count even number and return the sum of aall


def count_sum_of_all_even_numbers(numbers):
    sum=0

    for num in numbers:
        if num % 2 == 0:
            sum= sum + num
    return sum

result = count_sum_of_all_even_numbers([2, 7, 4, 9, 10, 3])

print (result)
