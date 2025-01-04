
expr3 = 0 and 1 # 0
print("expr3=", expr3)

expr4 = 3 and 9 # 9
print("expr4=", expr4)

expr4 = 3 and 9 and 13 # 13
print("expr4=", expr4)

expr4 = 3 and 13 and 9 # 9
print("expr4=", expr4) # If all non-zeros, results last element

expr5 = 0 or 1 # 1
print("expr5=", expr5)

expr6 = 3 or 9 # 3
print("expr6=", expr6)

expr6 = 3 or 9 or 13 # 3
print("expr6=", expr6)

expr6 = 13 or 9 or 3 # 13
print("expr6=", expr6) # or is resulting first element

expr6 = 0 or .0 or-9 or 3 # 9
print("expr6=", expr6) # first non-zero value


