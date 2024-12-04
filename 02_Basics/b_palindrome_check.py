"""
To check whether a string is palindrome or not 
palindrome strings
dad 
mom 

Algo 
1) Take the string from runtime and store in variable 
2) get the reverse string from the given string using the string reversal
3)compare both with a condition 


"""

test_string = input("Enter any string - ")
print("test string = ", test_string)

#reverse string
reverse_string = test_string[::-1]
print("reverse string = ", reverse_string)

print(test_string == reverse_string)

if test_string == reverse_string:
    print(test_string, "is palindrome")
else:
    print(test_string,'is not a palindrome')
    



