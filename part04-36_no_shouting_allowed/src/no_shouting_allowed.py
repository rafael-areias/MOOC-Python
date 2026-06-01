# Write your solution here
def no_shouting(my_list: list):
    new_list = []
    for l in my_list:
        if not l.isupper():
            new_list.append(l)
    return new_list
    
if __name__ == "__main__":
    print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))