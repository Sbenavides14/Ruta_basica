# ---------------------------------------
# Request the product name from the user
# This line asks the user to enter the name of the product
# ---------------------------------------
article = str(input("Enter the article name: "))

# ---------------------------------------
# Function to request and validate the price
# This function asks the user for the product price.
# If the user enters an invalid value (text or a number
# less than or equal to 0), the program shows an error
# message and asks again.
# ---------------------------------------
def price_required():
    try:
        price = float(input("Enter the price of the item: "))
        # Validate that the price is greater than 0
        if price <= 0:
            print("try again")
            return price_required()
    # Handle error if the user enters a non-numeric value
    except ValueError:
        print("try again")
        return price_required()
    return price

# ---------------------------------------
# Function to request and validate the quantity
# This function asks the user for the quantity of items.
# If the user enters an invalid value (text or a number
# less than or equal to 0), the program asks again.
# ---------------------------------------
def required_quantity():
    try:
        amount = int(input("Enter the amount: "))
        # Validate that the quantity is greater than 0
        if amount <= 0:
            print("try again")
            return required_quantity()
    # Handle error if the user enters a non-numeric value
    except ValueError:
        print("try again")
        return required_quantity()
    return amount

# ---------------------------------------
# Data input phase
# The functions are executed to obtain
# validated price and quantity values
# ---------------------------------------
price = price_required()
amount = required_quantity()

# ---------------------------------------
# Processing phase
# Calculate the total cost by multiplying
# the price by the quantity
# ---------------------------------------
total_cost = (price * amount)

# ---------------------------------------
# Output phase
# Display the results to the user
# ---------------------------------------
print(f"Product name: {article}")
print(f"Product price: {price}")
print(f"Product quantity: {amount}")
print(f"Total calculated cost: {total_cost}")

# -------------------------------------------------
# General program description
# -------------------------------------------------
# This program asks the user to enter the name of a product,
# its price, and the quantity. The system validates that the
# price and quantity are valid numeric values greater than zero.
# If the user enters an incorrect value, the program displays
# an error message and asks for the data again. Finally, it
# calculates the total cost by multiplying the price by the
# quantity and displays the product information along with
# the total cost.