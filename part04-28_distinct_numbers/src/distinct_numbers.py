# Write your solution here
def distinct_numbers(my_list: list):
    new = []
    for i in my_list:
        if i not in new:
            new.append(i)
    return sorted(new)

if __name__ == "__main__":
    print(distinct_numbers([3, 2, 2, 1, 3, 3, 1]))