# Functions For Each Operations

def addition(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a / b

# The Main Menu
print("Select Operation: ")
print("01.Addition")
print("02.Substraction")
print("03.Multiplication")
print("04.Division")


while True:
    x = input("Enter Choice (1/2/3/4): ")
    if x in ("1","2","3","4"):
        # Trying to catch errors
        try:
            num_1 = float(input("Enter Number 1: "))
            num_2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Invalid Input")
            continue

        # Addtions
        if (x == "1"):
            print(num_1, "+", num_2, "=", addition(num_1,num_2))

        # Subtract
        elif (x == "2"):
            print(num_1, "-", num_2, "=", substract(num_1,num_2))
            
        # Multiply
        elif (x == "3"):
            print(num_1, "x", num_2, "=", multiply(num_1,num_2))

        # Division 
        elif ( x == "4"):
            print(num_1, "x", num_2, "=", division(num_1,num_2))
        
        y = input("Do you wanna purpose another calculation? (Yes / No): ")
        if y == "no":
            break
    else:
        print("Invalid Input")

