# Write your solution here
def most_common_character(string):
    most_common = string[0]
    for i in string:
        if string.count(i) > string.count(most_common):
            most_common = i

    return most_common

if __name__ == "__main__":
    print(most_common_character("abcbde"))
    print(most_common_character("exemplaryelementary"))