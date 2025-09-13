import time
import sqlite3

def get_connection():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn):
    conn.close()

def main():
    start = time.perf_counter()

    class UserService:
        def get_user(self, user_id):
            conn, cursor = get_connection()
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            result = cursor.fetchone()
            close_connection(conn)
            return result

    class OrderService:
        def get_order(self, order_id):
            conn, cursor = get_connection()
            cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
            result = cursor.fetchall()
            close_connection(conn)
            return result

    # Fetches user
    user_service = UserService()
    user = user_service.get_user(2)
   
    # Fetches orders
    order_service = OrderService()
    order = order_service.get_order(2)
   
    end = time.perf_counter()
    print(f"Execution time: {end - start:.6f} seconds")


if __name__ == "__main__":
    main()
