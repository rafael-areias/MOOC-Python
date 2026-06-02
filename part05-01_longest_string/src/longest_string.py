# Write your solution here
def longest(strings: list):
    check_strings = ""
    for string in strings:
        if len(string) > len(check_strings):
            check_strings = string
    return check_strings


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))