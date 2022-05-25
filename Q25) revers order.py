N = int(input("Enter a three digit number:- "))
thirdDigit = N % 10
N = N // 10  # Removing last digit
secondDigit = N % 10
N = N // 10  # Removing last digit
firstDigit = N % 10

r = thirdDigit * 100 + secondDigit * 10 + firstDigit
