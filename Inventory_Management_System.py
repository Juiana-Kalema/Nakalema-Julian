# Inventory Management System using only for and while loops

inventory = {
    "Apples": 250,
    "Oranges": 150,
    "Grapes": 275,
    "Bananas": 451
}

def display_inventory():
    print("\n--- Current Inventory ---")
    item_found = False
    for item in inventory:
        print(f"{item}: {inventory[item]} units")
        item_found = True

    # If nothing was printed
    while not item_found:
        print("Inventory is empty.")
        break

def add_item():
    item = input("Enter item name to add: ").strip()
    item_exists = False
    for key in inventory:
        match = key == item
        while match:
            print(f"{item} already exists. Use 'Update' to change quantity.")
            item_exists = True
            break

    while not item_exists:
        quantity = input("Enter quantity: ")
        valid = True
        for amount in quantity:
            if amount not in "0123456789":
                valid = False

        while valid:
            inventory[item] = int(quantity)
            print(f"{item} added with {quantity} units.")
            break
        while not valid:
            print("Invalid input. Quantity must be numeric.")
            break
        break

def update_item():
    item = input("Enter item name to update: ").strip()
    found = False
    for key in inventory:
        match = key == item
        while match:
            quantity = input("Enter new quantity: ")
            valid = True
            for amount in quantity:
                if amount not in "0123456789":
                    valid = False

            while valid:
                inventory[item] = int(quantity)
                print(f"{item} updated to {quantity} units.")
                break
            while not valid:
                print("Invalid input. Quantity must be numeric.")
                break
            found = True
            break

    while not found:
        print(f"{item} not found in inventory.")
        break

def remove_item():
    item = input("Enter item name to remove: ").strip()
    removed = False
    keys = list(inventory.keys())
    for key in keys:
        match = key == item
        while match:
            del inventory[item]
            print(f"{item} removed from inventory.")
            removed = True
            break

    while not removed:
        print(f"{item} not found.")
        break

def exit_program():
    print("Exiting Inventory System. Goodbye!")
    global running
    running = False

# Menu option map (avoids if/elif/else)
menu_actions = {
    "1": display_inventory,
    "2": add_item,
    "3": update_item,
    "4": remove_item,
    "5": exit_program
}

# Main loop
running = True
while running:
    print("\n--- Inventory Menu ---")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    action_found = False
    for key in menu_actions:
        match = key == choice
        while match:
            menu_actions[key]()  # Call the correct function
            action_found = True
            break

    # If no matching action was found
    while not action_found:
        print("Invalid choice. Please select from 1 to 5.")
        break
