# To check whether a number is even or odd 

number = 32
print(f"{number          = }")
print(f"{number / 2      = }")
print(f"{number % 2      = }")
print(f"{number % 2 == 0 = }")

if number != 0:
    print(f"{number} is non-zero")

if number:
    print(f"{number} is non-zero")

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")