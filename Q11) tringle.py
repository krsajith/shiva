import math
S1 = int(input("Enter first side :- "))
S2 = int(input("Enter second side :- "))
S3 = int(input("Enter third side :- "))
A = (S1 + S2 + S3)
S = A/2
L = math.sqrt(S*(S-S1)*(S-S2)*(S-S3))
print(Area=L,)
