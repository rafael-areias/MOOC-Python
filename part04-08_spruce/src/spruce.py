# Write your solution here
def spruce(number):
    print("a spruce!")
    i = 1
    j = number -1
    while i < number * 2:
        print(" " * j + "*" * i)
        i += 2
        j -= 1
    print(" " * (number-1) + "*" * 1)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)



def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")