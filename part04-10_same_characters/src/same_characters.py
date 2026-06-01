# Write your solution here
def same_chars(text,i1,i2):
    if i1 > len(text) or i2 > len(text)-1:
        return False
    elif text[i1] == text[i2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))