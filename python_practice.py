numbers = [10, 20, 30, 40, 50]

total = 0
total_even = 0
for number in numbers:
    total += number

print("Total:", total)

for num in numbers:
    if num %2 == 0:
       total_even += num



print("Sum of total even number is", total_even)
