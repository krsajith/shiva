S1 = int(input("Enter side 1:- "))
S2 = int(input("Enter side 2:- "))
S3 = int(input("Enter side 3:- "))
if S1 + S2 < S3 and S2 + S3 < S1 and S1 + S3 < S1:
    print("It is a triangle ")
else:
    print("It is not a triangle")
