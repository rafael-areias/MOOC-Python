# Write your solution here
def all_the_longest(my_list: list):
    new = []
    for i in my_list:
        if new == [] or len(i) > len(new[0]):
            new = [i]
        elif len(i) == len(new[0]):
            new.append(i)
    return new

if __name__ == "__main__":
    print(all_the_longest(["first", "second", "fourth", "eleventh"]))
    print(all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))