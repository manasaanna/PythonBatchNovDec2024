"""
To check whether a sentence is palindrome or not


"""

test_sen = input("Enter a sentence - ")
print("the sentence is - ", test_sen)

#nospaces 
no_space = test_sen.replace(" ","")
print("sentence with no spaces" , no_space)

#reverse sentence 
reverse_sen = no_space[::-1]
print("reverse_sen = ", reverse_sen)

print(no_space == reverse_sen)

