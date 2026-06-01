# Write your solution here
def sum_of_positives(my_list: list):
    sum = 0
    for l in my_list:
        if l > 0:
            sum += l
    return sum
    

if __name__ == "__main__":
    print(sum_of_positives([1, -2, 3, -4, 5]))