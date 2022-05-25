S1 = int(input("Enter first side:- "))
S2 = int(input("Enter second side:- "))
S3 = int(input("Enter third side:- "))
if S1 == S2 == S3:
    print("it is a Equilateral triangle. ")
elif S1 == S2 or S2 == S3 or S3 == S1:
    print("it is a isosceles  triangle. ")
else:
    print("it is scalene triangle. ")

