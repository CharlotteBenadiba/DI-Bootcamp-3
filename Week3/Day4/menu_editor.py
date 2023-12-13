# Part 2
# Create a file called menu_editor.py , which will have the following functions:
# show_user_menu() - this function should display the program menu (not the restaurant 
# menu!), and ask the user to :
# View an Item (V)
# Add an Item (A)
# Delete an Item (D)
# Update an Item (U)
# Show the Menu (S)
# Call the appropriate function that matches the user’s input.

# add_item_to_menu() - this function should ask the user to input the item’s name and price. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was added successfully print a message which states: item was added successfully.

# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

# update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was updated successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

# show_restaurant_menu() - print the restaurant’s menu.

# When the user chooses to exit the program, display the restaurant menu and exit the program.

import psycopg2
from menu_manager import MenuManager
from menu_item import MenuItem 

def show_user_menu():
    print("Program Menu:")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit")

def add_item_to_menu():
    name = input("Enter the item's name: ")
    price = float(input("Enter the item's price: "))
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuItem.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")

def update_item_from_menu():
    old_name = input("Enter the name of the item to update: ")
    old_price = float(input("Enter the price of the item to update: "))
    new_name = input("Enter the new name for the item: ")
    new_price = float(input("Enter the new price for the item: "))
    
    item = MenuItem.get_by_name(old_name)
    if item and item.item_price == old_price:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Error: Item not found or incorrect price.")

def show_restaurant_menu():
    menu_items = MenuManager.all()
    print("Restaurant Menu:")
    for item in menu_items:
        print(f"{item.item_name}: ${item.item_price}")

if __name__ == "__main__":
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()

        if choice == "V":
            # View an Item
            name = input("Enter the name of the item to view: ")
            item = MenuItem.get_by_name(name)
            if item:
                print(f"Item: {item.item_name}, Price: ${item.item_price}")
            else:
                print("Error: Item not found.")

        elif choice == "A":
            # Add an Item
            add_item_to_menu()

        elif choice == "D":
            # Delete an Item
            remove_item_from_menu()

        elif choice == "U":
            # Update an Item
            update_item_from_menu()

        elif choice == "S":
            # Show the Menu
            show_restaurant_menu()

        elif choice == "E":
            # Exit the Program
            show_restaurant_menu()
            break

        else:
            print("Invalid choice. Please enter a valid option.")
