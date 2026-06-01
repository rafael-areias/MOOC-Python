# Write your solution here
sentence = []
i = 0
while True:
    word = input("Word: ")
    if word in sentence:
        print(f"You typed in {i} different words")
        break
    else:
        sentence.append(word)
    i += 1