from Connection import connect_to_DB
from mysql.connector import Error
try:
    # Attempt to connect
    connection = connect_to_DB()

    if connection and connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")


except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection safely
    try:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        print("MySQL connection closed.")
    except:
        pass
