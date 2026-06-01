# Write your solution here
limit = int(input("Limit: "))
number = 1
sum_value = 0
text = ""
while sum_value < limit:
    text += ("" if not text else " + ") + str(number)
    sum_value += number
    number += 1
print(f"The consecutive sum: {text} = {sum_value}")
 