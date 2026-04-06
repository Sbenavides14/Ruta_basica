"""
Advanced inventory menu with CSV persistence.
"""

import services
import files

def menu():
    inventory = []      # Main list where products are stored
    while True:
        # Main Menu
        print("\n=== Main Menu ===")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Find product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        option = input("Select an option (1-9): ")

        # Each option calls the corresponding function.
        if option == "1":
            services.add_product(inventory)

        elif option == "2":
            services.show_inventory(inventory)

        elif option == "3":
            services.find_product(inventory)

        elif option == "4":
            services.update_product(inventory)

        elif option == "5":
            services.delete_product(inventory)

        elif option == "6":
            services.calculate_statistics(inventory)

        elif option == "7":
            files.save_csv(inventory)

        elif option == "8":
            new_inventory = files.load_csv()
            if new_inventory:
                decision = input("Overwrite current inventory? (Y/N): ").upper()
                if decision == "Y":
                    inventory = new_inventory       # Overwrite inventory
                else:
                    inventory.extend(new_inventory) # Merge inventory

        elif option == "9":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")

# Program entry point
if __name__ == "__main__":
    menu()
