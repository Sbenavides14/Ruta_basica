"""
Functions for saving and loading inventory in CSV format.
"""

import csv

def save_csv(inventory):
    # Save the inventory to a CSV file by requesting the path via input.
    if not inventory:
        print("Inventory is empty, cannot save.")
        return

    path = input("CSV file path to save: ")     # It asks for the file path/name.
    try:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "price", "quantity"])  # Write a heading
            for p in inventory:
                writer.writerow([p["name"], p["price"], p["quantity"]])     # Write down each product
        print(f"Inventory saved to: {path}")
    except Exception as e:
        print(f"Error saving CSV: {e}")

def load_csv():
    # Load inventory from a CSV file by requesting the path via input.
    inventory = []
    errors = 0
    path = input("CSV file path to load: ")     # It asks for the file path/name.
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header != ["name", "price", "quantity"]:
                print("Invalid CSV header.")
                return []

            for row in reader:
                if len(row) != 3:
                    errors += 1
                    continue
                try:
                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])
                    if price < 0 or quantity < 0:
                        errors += 1
                        continue
                    inventory.append({"name": name, "price": price, "quantity": quantity})
                except ValueError:
                    errors += 1
                    continue

        print(f"Inventory loaded from: {path}")
        if errors > 0:
            print(f"{errors} invalid rows omitted.")
        return inventory
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading CSV: {e}")
    return []
