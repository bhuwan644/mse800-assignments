import sqlite3

# Connect to (or create) a database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create a users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_name TEXT NOT NULL UNIQUE
)
""")

# Insert a new user
def create_user(username, email, password):
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                       (username, email, password))
        conn.commit()
        print("User created successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username or Email already exists.")
        
def create_order(order_name):
    try:
        cursor.execute("INSERT INTO orders (order_name) VALUES (?)",
                       (order_name,))  
        conn.commit()
        print("Order created successfully!")
    except sqlite3.IntegrityError:
        print("Error: Order already exists.")

# Example usage
create_user("john_doe", "john@example.com", "123")
create_user("Bhuwan", "a@example.com", "111")
create_user("Dipak", "b@example.com", "333")
create_user("c", "c@example.com", "444")
create_user("d", "d@example.com", "555")
create_user("e", "e@example.com", "666")


create_order("Banana")
create_order("Fruit")
create_order("Ripe")
create_order("Grapes")

order_list=cursor.execute("SELECT * FROM orders")
for row in cursor.fetchall():
    print(row)



# Fetch and display users


# Close the connection
conn.close()
