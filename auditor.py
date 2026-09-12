inventory = 0

# Loop to continuously prompt the user for input until they choose to exit
while True:
    user_input = input("Please enter the number of items to add to inventory (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    items_to_add = int(user_input)
    inventory += items_to_add
    print(f"Inventory updated. Current stock: {inventory}")
