"""
Apples = 12/piece, 5 dozen total no. = 5*12 = 60 total amount = 60 * 12 = 720
Mangoes = 34/piece, 3 dozen total no. = 3*12 = 36 total amount = 36 * 34 = 1224

discount - 2%
GST - +12.5%

Algorithm

1) cost of the fruits into variables
2) quantity of fruit into variables
3) compute the end quantity by substituting dozen value
4) compute the selling price of each item 
5) calculate discount and substract 
6) calculate the gst and add it to the amount

"""
#constants
DOZEN = 12
DISCOUNT = 2
GST = 12.5

cost_of_apple = 12
cost_of_mango = 34

qty_of_apples = DOZEN  * 5
qty_of_mangoes = DOZEN  * 3

#selling price computation 
total_sp = (cost_of_apple * qty_of_apples) + (cost_of_mango * qty_of_mangoes)
print("total selling price : ", total_sp)

#discount
discount_amount = (total_sp * DISCOUNT)/100
print("Discount Amount : ", discount_amount)

#payable amount 
payable_amount = total_sp - discount_amount
print("Payable Amount : ", payable_amount)

#GST Calculation - PEMDAS
gst_on_fruits = payable_amount * GST/100
print("GST on fruits : ", gst_on_fruits)

#Total amount
total_amount = payable_amount + gst_on_fruits
print("Total Amount : ", total_amount)

#round
print("Total Amount : ", round(total_amount,2))




