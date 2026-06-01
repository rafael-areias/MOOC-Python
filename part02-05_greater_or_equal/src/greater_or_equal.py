num1 = int(input("Please type in a number: "))
num2 = int(input("Please type in another number: "))

if num1 > num2:
    print(f"The greater number was: {num1}")
elif num2 > num1:
    print(f"The greater number was: {num2}")
else:
    print("The numbers are equal!")