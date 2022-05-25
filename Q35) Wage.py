Age = int(input("Enter age:- "))
S = input("Enter sex (M/F):-")
D = int(input("Enter the no day worked:- "))

amount = 0

if 18 <= Age <= 30:
    if S.upper() == "M":
        amount = D * 750
    else:
        amount = D * 700
elif 30 <= Age <= 40:
    if S.upper() == "M":
        amount = D * 850
    else:
        amount = D * 800

print(amount)
