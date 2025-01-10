import sys
# Progress bar implementation
for progress in range(3,101, 7):
    stars = "*" * (progress // 10) # Number of stars increases with progress
    spaces = " " * (10 - progress // 10)  # Remaining spaces
    print(f"[{stars}{spaces}] {progress}")
    break
for progress in range(10,101, 10):
    stars = "*" * (progress // 10) # Number of stars increases with progress
    spaces = " " * (10 - progress // 10)  # Remaining spaces
    print(f"[{stars}{spaces}] {progress}")  

   
