# Write your solution here
def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for s in string:
        if s not in vowels:
            new_string += s
    return new_string

if __name__ == "__main__":
    print(no_vowels("this is an example"))