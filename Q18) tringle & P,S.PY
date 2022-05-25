S1 = int(input("Enter side 1:- "))
S2 = int(input("Enter side 2:- "))
S3 = int(input("Enter side 3:- "))
if S1 + S2 < S3 and S2 + S3 < S1 and S1 + S3 < S1:
    print("It is a triangle ")
P = S1 + S2 + S3
S = P / 2
A = (S * (S - S1) * (S - S2) * (S - S3)) ** 0.5
print("Area:-", A, "Perimeter:-", P)
if P > A:
    print("Perimeter is bigger than area")
elif P < A:
    print("Area is bigger than perimeter")
