# Write your solution here
def even_numbers(my_list: list):
    new_list = []
    for l in my_list:
        if l % 2 == 0:
            new_list.append(l)
    return new_list

if __name__ == "__main__":
    print(even_numbers([1, 2, 3, 4, 5]))
