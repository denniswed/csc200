# CSC200-1 Critical Thinking Module 2
def add_numbers(x,y):
    return x + y

def multiple_numbers(x,y):
    return x * y

def divide_numbers(x,y):
    return x / y

def subtract_numbers(x,y):
    return x - y

def get_input():
    print("Hello!\nYou will be prompted to provide two numbers.\nThese numbers can be any integer or decimal except you cannot use 0 (zero).")
    while True:
        number1 = float(input("Please provide your first number. "))
        if number1 == 0:
            print("Please type a number OTHER than 0 (zero).")
            continue
        else:
            break
    
    while True:
        number2 = float(input("Please provide your second number. "))
        if number2 == 0:
            print("Please type a number OTHER than 0 (zero).")
            continue
        else:
            break
    
    return number1, number2

number1, number2 = get_input()
added_numbers = add_numbers(number1,number2)
multiplied_numbers = multiple_numbers(number1,number2)
divided_numbers = divide_numbers(number1,number2)
subtracted_numbers = subtract_numbers(number1,number2)

print("You supplied numbers", str(number1), "and ", end='')
print(str(number2), ".", sep='')
print(number1, "+", number2, "=", added_numbers)
print(number1, "-", number2, "=", subtracted_numbers)
print(number1, "*", number2, "=", multiplied_numbers)
print(number1, "/", number2, "=", divided_numbers)
