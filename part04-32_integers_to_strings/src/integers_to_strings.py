# Write your solution here
def formatted(my_list: list):
    new = []
    for i in my_list:
        i = f"{i:.2f}"
        new.append(i)
    return new

if __name__ == "__main__":
    print(formatted([1.234, 0.3333, 0.11111, 3.446]))