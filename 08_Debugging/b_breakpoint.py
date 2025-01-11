val_1 = int(input("Enter val_1 :"))
val_2 = int(input("Enter val_2 :"))

breakpoint()

result = val_1 * val_2
print(f"Multiplication :{result}")



numbers = range(0, 100)

# import pdb; pdb.set_trace()
# breakpoint()

# To Display all even numbers
for each_num in numbers:
    if each_num % 2 == 0: #each_num % 2:
        print(each_num)

# Post Analysis

# python -i SCRIPTNAME.py