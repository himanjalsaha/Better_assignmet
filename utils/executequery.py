import sqlite3
from .connectdb import get_db_connection
def execute_query(query, params=None, fetch=False):
            try:
                connection = get_db_connection()
                cursor = connection.cursor()
                cursor.execute(query, params or ())
                if fetch:
                    rows = cursor.fetchall()
                    return rows
                connection.commit()
            except sqlite3.Error as e:
                print(f"Database error: {e}")
            finally:
                if connection:
                    connection.close()