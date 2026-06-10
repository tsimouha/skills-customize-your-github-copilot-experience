# Starter Code: Python Persistence with SQLite

import sqlite3
from sqlite3 import Connection

DB_FILE = "app_data.db"


def create_connection(db_file: str = DB_FILE) -> Connection:
    conn = sqlite3.connect(db_file)
    return conn


def initialize_database(conn: Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            notes TEXT
        )
        """
    )
    conn.commit()


def add_item(conn: Connection, name: str, quantity: int, notes: str) -> None:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, quantity, notes) VALUES (?, ?, ?)",
        (name, quantity, notes),
    )
    conn.commit()


def list_items(conn: Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, quantity, notes FROM items")
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    connection = create_connection()
    initialize_database(connection)
    print("Database initialized. Add your application logic here.")
    connection.close()
