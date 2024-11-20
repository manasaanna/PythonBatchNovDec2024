"""
1) we can take the input from the user about the initial amt,time,rate
2) then we can calculate the simple intrest
3) then add the simple intrest to the initial amount and then we get the final amount 

"""
#Initial amount
initial_amt = input("Please enter the initial amount = " )
initial_amt = float(initial_amt)
print("The initial amount is : ", initial_amt)

#rate
rate = input("Please enter the rate (in %) = ")
rate = float(rate)
print("The rate is : ", rate)

#time 
time = input("Please enter the time period ( in yrs)= ")
time = float(time)
print("The time period is : ", time)

#simple intrest 
smpl_interest = (initial_amt * rate * time)/100

#final amount 
final_amt = initial_amt + smpl_interest

print(final_amt)



