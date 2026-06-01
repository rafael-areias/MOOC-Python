# Write your solution here
def shortest(my_list: list):
    length = ""
    for i in my_list:
        if len(length) == 0:
            length = i
        elif len(i) < len(length):
            length = i
    return length

if __name__ == "__main__":
    print(shortest(["first", "second", "fourth", "eleventh"]))
    print(shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))