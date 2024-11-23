# Menu items dictionary
menu_items = {"beer": 5.00, "wine": 8.00, "cola": 3.00}

# Set up order list
order_list = []

# Display the menu
print("Welcome to The Handle Bar!")
print("Menu:")
print("-" * 30)

# Number the items
for i, (item, price) in enumerate(menu_items.items(), start=1):
    print(f"{i}. {item} - ${price:.2f}")

print("-" * 33)

# Main loop for ordering
while True:
    menu_selection = input("Please enter the number of the item you'd like to order: ")

    # Check if input is a number
    if not menu_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue  # Restart the loop

    menu_selection = int(menu_selection)
    if menu_selection < 1 or menu_selection > len(menu_items):
        print("Invalid input. Please choose a valid menu item.")
        continue  # Restart the loop

    # Get the selected item
    item_name = list(menu_items.keys())[menu_selection - 1]
    item_price = menu_items[item_name]
    print(f"You selected {item_name}, which costs ${item_price:.2f}")

    # Check if the quantity is valid; if not, default to 1
    quantity_input = input(f"How many {item_name}(s) would you like? (Default is 1 if input is invalid): ")
    if quantity_input.isdigit():
        quantity = int(quantity_input)
    else:
        quantity = 1

    # Append the customer's order to the order list in dictionary format
    customer_order = {"item name": item_name, "item price": item_price, "quantity": quantity}
    order_list.append(customer_order)

    # Ask the customer if they would like to keep ordering
    while True:
        order_more = input("Would you like to place another order? (y/n): ").lower()
        match order_more:
            case "y":
                break  # Break out of the inner loop and continue ordering
            case "n":
                # Generate the receipt and exit
                print("\nThank you for your order!")
                print("Your Receipt:")
                print("-" * 33)
                total_cost = 0
                total_cost = sum(order["item price"] * order["quantity"] for order in order_list)
                for order in order_list:
                    print(f"{order['item name'].ljust(20)} | ${order['item price']:.2f} | x{order['quantity']}")
                print("-" * 33)
                print(f"Total cost: ${total_cost:.2f}")
                exit()  # Exit the program
