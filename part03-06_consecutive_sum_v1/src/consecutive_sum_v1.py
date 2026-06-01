# Write your solution here
limit = int(input("Limit: "))
number = 1
sum_value = 0
while sum_value < limit:
    sum_value += number
    number += 1
print(sum_value)