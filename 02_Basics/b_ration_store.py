"""
Purpose - ration store
wheat = 25/kg, 30
Rice = 12/kg, 50

Subsidy 20%

Algorithm 
1) get the cost of items into variables
2) get the quantity of items into variables
3) compute the selling price of each item, and add them 
4) compute the subsidy amount and substract it form the selling price 
5) Display the billable amount

"""
#cost of items
cost_of_wheat = 25
cost_of_rice = 12

#Quatities of items
qty_of_wheat = 30
qty_of_rice = 50

#selling price computation 
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice
print(total_sp)

subsidy_amount = (total_sp * 20)/100
print("subsidy Amount : ",subsidy_amount )

billable_amount = total_sp - subsidy_amount
print("Billable Amount : ",billable_amount )

