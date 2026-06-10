# 📘 Assignment: Python Persistence with SQLite

## 🎯 Objective

Build a Python application that stores, retrieves, and updates data in a local SQLite database to learn persistence, CRUD operations, and database schema design.

## 📝 Tasks

### 🛠️ Initialize the SQLite database

#### Description
Create a local SQLite database and define a table to store items or records for the application.

#### Requirements
Completed program should:

- Create or open a SQLite database file using `sqlite3`.
- Define a table with at least three columns, including an integer primary key.
- Ensure the table is created only once and does not fail if it already exists.

### 🛠️ Implement CRUD operations

#### Description
Add functions to create, read, update, and delete records in the database.

#### Requirements
Completed program should:

- Insert new records into the table using parameterized SQL.
- Retrieve and display all records from the table.
- Update an existing record by its ID.
- Delete a record by its ID.

### 🛠️ Add validation and user interaction

#### Description
Build a simple console menu that lets the user choose actions and validates inputs before using the database.

#### Requirements
Completed program should:

- Display a menu with options for adding, listing, updating, and deleting records.
- Validate user input and show clear messages for invalid choices or missing records.
- Close the database connection cleanly when the program exits.
