# Write your solution here
def list_sum(list1, list2):
    new = []
    for l in range(len(list1)):
        new.append(list1[l]+list2[l])
    return new

if __name__ == "__main__":
    print(list_sum([1, 2, 3],[7, 8, 9]))
