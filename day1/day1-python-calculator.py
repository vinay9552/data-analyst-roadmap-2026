def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0:
        return "Error: Divisor cannot be zero"
    return x/y

print("==== Python Calcuator ====")

while True:
    try:
        num1 = float(input("Enter First number: "))
        num2 = float(input("Enter Second number: "))
        operation = input("Enter operator (+,-,*,/):")

        if operation == "+":
            print(f"result : {add (num1, num2)}") 
        elif operation == "-":
            print(f"Result : {sub(num1,num2)}")
        elif operation == "*":
            print(f"Result: {mul(num1,num2)}")
        elif operation == "/":
            print(f"Result : {div(num1,num2)}")
        else :
            print('Invalid Operator')
    except ValueError:
        print("Enter a Valid number")
    choise = input("Do you want to perform another operation (y/n):").lower()

    if choise == "n":
        print("Thank you")
        break
