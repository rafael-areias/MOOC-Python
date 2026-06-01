# Write your solution here
my_list = []
times = int(input("How many times: "))
i = 1
while i <= times:
    item = int(input(f"Item {i}: "))
    my_list.append(item)
    i += 1
print(my_list)