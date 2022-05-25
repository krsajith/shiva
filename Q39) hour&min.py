H1 = int(input("Enter amount of hour of first work:- "))
M1 = int(input("Enter amount of minute of first work:- "))
H2 = int(input("Enter amount of hour of second work:- "))
M2 = int(input("Enter amount of minute of second work:- "))
H = H1 + H2
M = M1 + M2

if M > 60:
    H = H - 1
    M = M - 60

    print("total time is", H, "hours and", M, "minutes.")

