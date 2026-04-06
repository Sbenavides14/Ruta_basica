\# Inventory System in Python

This project is a simple console-based inventory management system. It was built as a learning exercise to practice Python fundamentals such as functions, loops, conditionals, error handling, and working with CSV files.

\## Description

The program allows you to manage a list of products, each with a name, price, and quantity. It includes basic CRUD operations (Create, Read, Update, Delete), inventory statistics, and the ability to save and load data using CSV files. The code is modular, with separate files for services (CRUD and statistics) and file handling (CSV operations).

\## How it works

The program runs in the terminal and follows this process:

1. Display the main menu with options from 1 to 9.
1. Ask the user to choose an option.
1. Perform the selected action:
- `1`: Add a product.
- `2`: Show all products in the inventory.
- `3`: Find a product by name.
- `4`: Update a product’s price or quantity.
- `5`: Delete a product.
- `6`: Show inventory statistics (total units, total value, most expensive product, largest stock).
- `7`: Save the inventory to a CSV file.
- `8`: Load inventory from a CSV file (overwrite or merge).
- `9`: Exit the program.

4\. Validate inputs and show feedback messages.

5\. Repeat until the user chooses to exit.

\## Code Status

The project works well and achieves its main goal: managing an inventory through the console, saving and loading data in CSV files, and performing basic operations such as adding, searching, updating, and deleting products.
