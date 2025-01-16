import sys
stack = []

while True:
    print("\n1. Push\n2. Pop\n3. Status\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:  # Push
        value = input("Enter the value to push: ")
        stack.append(value)
        print(f"Pushed {value} to the stack.")

    elif choice == 2:  # Pop
        if len(stack) == 0:
            print("Stack is empty! Nothing to pop.")
        else:
            removed = stack.pop()
            print(f"Popped {removed} from the stack.")

    elif choice == 3:  # Status
        print(f"Stack size: {len(stack)}")
        print(f"Stack elements: {stack}")

    elif choice == 4:  # Exit
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")

    sys.exit()