N = int(input("Enter a three digit number :- "))
thirddigit = N % 10
secondigit = N % 100 // 10
firstdigit = N // 100
S = firstdigit + secondigit + thirddigit
print(S)

