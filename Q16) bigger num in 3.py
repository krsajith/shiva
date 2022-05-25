num1 = int(input("Enter first no :- "))
num2 = int(input("Enter second no :- "))
num3 = int(input("Enter third no :- "))
if num2 < num1 > num3:
    print(num1, " is bigger")
elif num1 < num2 > num3:
    print(num2, " is bigger")
elif num1 < num3 > num2:
    print(num3, " is bigger")
