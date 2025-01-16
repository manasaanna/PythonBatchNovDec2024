import sys
queue = []

while True:
    print("\n1. Push\n2. Pop\n3. Status\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:  # Push
        value = input("Enter the value to push: ")
        queue.insert(0, value)
        print(f"Pushed {value} to the queue.")

    elif choice == 2:  # Pop
        if len(queue) == 0:
            print("Queue is empty! Nothing to pop.")
        else:
            removed = queue.pop()
            print(f"Popped {removed} from the queue.")

    elif choice == 3:  # Status
        print(f"Queue size: {len(queue)}")
        print(f"Queue elements: {queue}")

    elif choice == 4:  # Exit
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
    
    sys.exit()