num1 = int(input("Enter first no :- "))
num2 = int(input("Enter second no :- "))
if num2 == 0:
    print("Division by zero")
else:
    if num1 % num2 == 0:
        print("yes")
    else:
        print("no")
