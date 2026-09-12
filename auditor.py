inventory = 0

# Loop to continuously prompt the user for input until they choose to exit
while True:
    user_input = input("\nPlease enter the number of items to add to inventory (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    # Checks for handle invalid input (non-integer values)    
    if not user_input.isdigit():
        print("Invalid input. Please enter an integer number or type 'exit'.")
        continue

    items_to_add = int(user_input) # Convert the user input to an integer
    inventory += items_to_add
    print(f"Inventory updated. Current stock: {inventory}")

 

