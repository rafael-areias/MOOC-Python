# Write your solution here
my_list = []
while True:
    print(f"The list is now {my_list}")
    a_r_x = input("a(d)d, (r)emove or e(x)it: ")
    if a_r_x == "x":
        print("Bye!")
        break
    elif a_r_x == "d":
        if len(my_list) == 0:
            my_list.append(1)
        else:
            my_list.append(len(my_list)+1)
    elif a_r_x == "r":
        my_list.pop(-1)
