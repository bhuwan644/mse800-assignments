import time
import sqlite3

def main():
    start = time.perf_counter() ## To store start time of program execution

    class UserService:
        def get_user(self, user_id):
            conn=sqlite3.connect('mydatabase.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM users where id=?",(user_id,))
            result=cursor.fetchone()
            conn.close()
            return result


    class OrderService:
        def get_user(self, user_id):
            conn=sqlite3.connect('mydatabase.db')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM orders where id=?",(user_id,))
            result=cursor.fetchall()
            conn.close()
            return result


    ##### Fetches user list
    user_service=UserService()
    user=user_service.get_user(2)
   
    ##### Fetches order list
    order_service=OrderService()
    order=order_service.get_user(2)
   
    end = time.perf_counter()

    ## Printing out the total execution time
    print(f"Execution time for this entire code to execute is: {end - start:.6f} seconds")



if __name__=="__main__":
    main()


