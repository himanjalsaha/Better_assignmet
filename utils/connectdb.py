import sqlite3



DB_PATH = "library.db"

def get_db_connection():
        try:
            connection = sqlite3.connect(DB_PATH)
            connection.row_factory = sqlite3.Row  # Access rows as dictionaries
            return connection
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise


 
    
