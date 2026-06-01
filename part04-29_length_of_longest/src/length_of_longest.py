# Write your solution here
def length_of_longest(my_list: list):
    longest = 0
    for item in my_list:
        item = int(len(item))
        if item > longest:
            longest = item
    return longest

if __name__ == "__main__":
    print(length_of_longest(["first", "second", "fourth", "eleventh"]))
    print(length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))

