first = 1
while first <= 10:
    print(f"Multiplication Table for {first}:")
    
    second = 1
    while second <= 10:
        print(f"\t{first} x {second} = {first * second}")
        second += 1  # Increment inner loop
    
    print("-" * 20)  # Separator for better readability
    first += 1

first = 1
while first <= 10:
    second = 1
    while second <= 10:
        print(f"{first} x {second} = {first * second}", end="\t")  # Print horizontally with tabs
        second += 1
    print()  # Move to the next line after completing one table
    first += 1

    