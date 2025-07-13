import mysql.connector

def connect_to_DB():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Or your actual MySQL root password
        )
        return connection
    except Error as e:
        print("Failed to connect to MySQL:", e)
        raise


