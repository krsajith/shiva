N = int(input("Enter a three digit no :- "))
m = N
thirdigit = N % 10
N = N // 10
seconddigit = N % 10
N = N // 10
firstdigit = N % 10
N = N // 10
r = thirdigit * 100 + seconddigit * 10 + firstdigit
if m == r:
    print(m, "is a palindrome")
else:
    print(m, "is not a palindrome")
