import mysql.connector

def connect_to_DB():
    return mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="",
        database ="alx_book_store",
        port = 3306
    )


