"""
compound interest
1) number of times the compound interest is applied
2) calculate the interest and the total amount

"""


pripl_amt = input("Enter the principal amount : ")
pripl_amt = float(pripl_amt)
print("The principal amount is : ", pripl_amt)

rate = input("Enter the rate ( in %) : ")
rate = float(rate)
print("The rate is : ", rate)

time = input("Enter the time (in yrs) : ")
time = float(time)
print("The time is : ", time)

#convert the rate as it is anualy
rate = rate / 100

n = input("Enter the no. of times the interest is compounded : ")
n = float(n)

amount = pripl_amt * (1 + rate/n) ** (n * time)
compd_intrst = amount - pripl_amt

print(round(compd_intrst,2))

total_amt = compd_intrst + pripl_amt
print(round(total_amt,2))
