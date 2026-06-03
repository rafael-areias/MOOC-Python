# Write your solution here
def double_items(numbers: list):
    new_numbers = []
    for number in numbers:
        double = number * 2
        new_numbers.append(double)

    return new_numbers

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)


## Solution

def double_items(numbers: list):
    double = numbers[:]
    for i in range(len(double)):
        double[i] *= 2
    
    return double