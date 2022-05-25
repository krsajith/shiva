S1 = int(input("Enter mark of first subject:-  "))
S2 = int(input("Enter mak of second subject:- "))
S3 = int(input("Enter mark of third subject:- "))
if S1 >= 40 & S2 >= 40 & S3 >= 40:
    print("passed")
elif S1 + S2 + S3:
    print("promoted")
elif S1 + S2 + S3 + 5:
    print("Promoted with moderation")
else:
    print("failed")
