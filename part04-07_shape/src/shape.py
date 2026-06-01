# Copy here code of line function from previous exercise and use it in your solution
def line(number,symbol):
    if symbol == "":
        print("*" * number)
    else:
        print(symbol[0] * number)
    
def shape(size, symbol, second_size, secon_symbol):
    i = 1
    while i <= size:
        line(i, symbol)
        i += 1
    j = 1
    while j <= second_size:
        line(size,secon_symbol)
        j += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")