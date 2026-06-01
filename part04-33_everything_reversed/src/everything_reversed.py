# Write your solution here
def everything_reversed(my_list: list):
    new = []
    for i in my_list:
        new.append(i[::-1])
    return new[::-1]

if __name__ == "__main__":
    print(everything_reversed(["Hi", "there", "example", "one more"]))