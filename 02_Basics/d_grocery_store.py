"""
rice = 10/kg
wheat = 34/kg

Algorithm 
1) cost of the items into variables
2) get the quatity of items from the user (in run-time)

Note - input() - to get the value in run-time
                 will give any input as string only
"""
#cost of items
cost_of_rice = 10
cost_of_wheat = 34

#quatity of items
qty_of_rice = input("Enter quatity of rice (in kgs)")
qty_of_rice = float(qty_of_rice)
print("Quantity of rice : ", qty_of_rice)

qty_of_wheat = float(input("Enter quatity of wheat (in kgs) : "))

#selling price of computation
sp_of_rice = cost_of_rice * qty_of_rice
print("SP of rice : " , sp_of_rice) 

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("SP of wheat : " , sp_of_wheat) 

#Total
total_sp = sp_of_rice + sp_of_wheat
print("total SP : ", total_sp)
