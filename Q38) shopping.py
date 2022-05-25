N = (input("Enter you name:- "))
i = int(input("Enter number of item:- "))
C = int(input("Enter cost of item:- "))

Total = i*C

if Total >= 1000:
    print("your total", Total*(98/100), "you got a discount of 2%")
elif Total >= 3000:
    print("your total", Total*(97/100), "you got a discount of 3%")
else:
    print("your total is", Total)
