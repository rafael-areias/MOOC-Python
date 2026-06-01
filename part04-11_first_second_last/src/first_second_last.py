# Write your solution here
def first_word(text):
    idx = text.find(" ")
    return text[:idx]

def second_word(text):
    space = text.find(" ")
    text = text[space+1:]
    second_space = text.find(" ")

    if second_space == -1:
        return text
    return text[:second_space]
    

def last_word(text):
    idx = 0
    while idx != -1:
        text = text[idx+1:]
        idx = text.find(" ")
    return text

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "happily ever after"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))