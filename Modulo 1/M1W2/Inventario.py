# Global list where products are stored
inventory= []

def main():
    # Main function that executes the menu in a loop
    while True:
        print("----------------------------")

        print("\n--- MENU ---")
        print("1. Add product")             # Option to add product      
        print("2. Show inventory")          # Option to display inventory
        print("3. Calculate statistics")    # Option to calculate statistics
        print("4. Exit")                    # Exit option

        option = input("Choose an option: ")
        print("---------------------------")

        # Conditionals to execute the chosen option
        if option == "1":
            add_product()
        elif option == "2":
            show_inventory()
        elif option == "3":
            calculate_statistics()
        elif option == "4":
            print("See you soon")
            break
        else:
            print("Invalid option")         # Message if the user enters something incorrect


def add_product():
    # Function to add a product to the inventory
    name = input("Product Name: ")          # Product Name
    price = price_validation()              # Price validation
    quantity = quantity_validation()        # Quantity validation

    # The product is saved as a dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory.append(product)               # The product is added to the global list
    print("Added product")


def show_inventory():
    # Function to display all products in inventory
    if len(inventory) == 0:
        print("Empty inventory")
        return
    # Scroll through the list and show each product with an index
    for index, attribute in enumerate(inventory):
        print(f"{index + 1}. Name: {attribute['name']}, Price: {attribute['price']}, Quantity: {attribute['quantity']}")


def calculate_statistics():
    # Function to calculate inventory statistics
    if len(inventory) == 0:
        print("Empty inventory")
        return 

    total_value = 0                         # Total inventory value
    total_products = 0                      # Total quantity of products

    # Browse each product and accumulate values
    for attribute in inventory:
        total_value += attribute["price"] * attribute["quantity"]
        total_products += attribute["quantity"]

    print(f"Total inventory value: {total_value}")
    print(f"Total number of products: {total_products}")


def price_validation():
    # Function to validate that the price is a number greater than 0
    while True:
        try:
            price = float(input("Product price: "))
            if price <= 0:
                print("Price must be greater than 0, please try again.")
            else:
                return price
        except ValueError:
            print("You must enter a valid number, please try again")


def quantity_validation():
    # Function to validate that the quantity is an integer greater than 0
    while True:
        try:
            quantity = int(input("Product quantity: "))
            if quantity <= 0:
                print("The amount must be greater than 0, please try again.")
            else:
                return quantity
        except ValueError:
            print("You must enter a valid number, please try again.")
            
# Call to the main function to start the program
main() 