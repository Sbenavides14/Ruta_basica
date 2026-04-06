"""
CRUD functions and inventory statistics.
"""

def add_product(inventory):
    # Request user data to create a product
    name = input("Name: ")
    try:
        price = float(input("Price: "))         # Convert the price to a decimal number
        quantity = int(input("Quantity: "))     # Convert the amount to a whole number
        if price < 0 or quantity < 0:           # Validation: Negative values ​​are not allowed
            print("Price and quantity must be non-negative.")
            return
        # Create a dictionary with the product data 
        product = {"name": name, "price": price, "quantity": quantity}
        # Add it to the inventory list
        inventory.append(product)
        print(f"Product '{name}' added successfully.")
    except ValueError:
        # If the user enters something other than a number, it displays an error.
        print("Invalid input. Price and quantity must be numeric.")


def show_inventory(inventory):
    # Shows all products in inventory
    if not inventory:
        print("Inventory is empty.")
    else:
        for p in inventory:
            print(f"{p['name']} - Price: {p['price']} - Quantity: {p['quantity']}")

def find_product(inventory):
    # Search for a product by name
    name = input("Name to search: ")
    for p in inventory:
        if p["name"].lower() == name.lower():  # Comparison regardless of uppercase/lowercase
            print(p)
            return p
    print("Product not found.")
    return None

def update_product(inventory):
    # Update the price and/or quantity of a product
    name = input("Name to update: ")
    product = None
    for p in inventory:
        if p["name"].lower() == name.lower():
            product = p
            break
    if product:
        # Request new values; if left blank, they will not be changed.
        new_price = input("New price (leave empty to skip): ")
        new_quantity = input("New quantity (leave empty to skip): ")
        try:
            if new_price:
                product["price"] = float(new_price)
            if new_quantity:
                product["quantity"] = int(new_quantity)
            print(f"Product '{name}' updated.")
        except ValueError:
            print("Invalid input.")
    else:
        print("Product not found.")

def delete_product(inventory):
    # Remove a product from the inventory
    name = input("Name to delete: ")
    product = None
    for p in inventory:
        if p["name"].lower() == name.lower():
            product = p
            break
    if product:
        inventory.remove(product)           # Remove the product from the list
        print(f"Product '{name}' deleted.")
    else:
        print("Product not found.")

def calculate_statistics(inventory):
    # Calculate basic inventory statistics
    if not inventory:
        print("Inventory is empty.")
        return

    # Accumulator variables
    total_units = 0
    total_value = 0

    # We begin with the first product
    most_expensive = inventory[0]
    largest_stock = inventory[0]

    # We iterate through the inventory using a for loop
    for product in inventory:
        # Adding quantities
        total_units = total_units + product["quantity"]

        # Add up total value (price * quantity)
        total_value = total_value + (product["price"] * product["quantity"])

        # Compare prices to find the most expensive one.
        if product["price"] > most_expensive["price"]:
            most_expensive = product

        # Compare quantities to find more stock
        if product["quantity"] > largest_stock["quantity"]:
            largest_stock = product

    # Show results
    print("=== Inventory Statistics ===")
    print(f"Total units: {total_units}")
    print(f"Total value: {total_value}")
    print(f"Most expensive product: {most_expensive['name']} (${most_expensive['price']})")
    print(f"Product with largest stock: {largest_stock['name']} ({largest_stock['quantity']})")

