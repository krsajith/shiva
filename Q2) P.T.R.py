T = int(input("Enter principle amount:- "))
R = int(input("Enter rate of interest:- "))
P = int(input("Enter number of years:- "))
SI = (P*R*T/100)
amount = T + SI
print("Simple interest:-", SI)
print("Total amount to be paid:-", amount)
