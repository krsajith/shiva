cost = int(input("Enter bike cost:- "))
if cost >= 100000:
    tax = cost/100*15
elif cost >= 50000:
    tax = cost/100*10
else:
    tax = cost/100*5
print(tax)
