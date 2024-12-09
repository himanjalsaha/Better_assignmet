from models.book import BookModel

from queries.book_queries import book_queries
from utils import execute_query
class Books_services:


    @staticmethod
    def create_books_table():
        query = book_queries.create_books
        execute_query(query)

    @staticmethod
    def add_book(title, author, year, genre ,  borrowed_by , ISBN):
        query = book_queries.add_books
        execute_query(query, (title, author, year, genre , borrowed_by , ISBN))

    @staticmethod
    def get_all_books():
        query = book_queries.get_all_books
        rows = execute_query(query, fetch=True)
        return [BookModel(row["id"], row["title"], row["author"], row["year"], row["genre"] , row["borrowed_by"] , row["ISBN"]) for row in rows]

    @staticmethod
    def update_book(book_id, title, author, year, genre, borrowed_by, ISBN):
        query = book_queries.update_books
        try:
            # Ensure that the parameters are passed as a tuple
            execute_query(query, (title, author, year, genre, borrowed_by, ISBN, book_id))
            return True 
        except Exception as e:
            print(f"Error: {e}")
            return False  
        
    @staticmethod
    def get_book_by_id(book_id):
        query = book_queries.book_by_id
        row = execute_query(query, (book_id,), fetch=True)  # Ensure it's passed as a tuple
        if row:
            row = row[0]  # Since we're expecting only one result
            return BookModel(
                row["id"], 
                row["title"], 
                row["author"], 
                row["year"], 
                row["genre"], 
                row["borrowed_by"], 
                row["ISBN"]
            )
        return None  # Or handle the case when no book is found


    def delete_book(book_id):
        query = book_queries.delete_book
        try:
            execute_query(query, (book_id,))
            return True  
        except Exception as e:
            print(f"Error: {e}")
            return False 
    
    @staticmethod
    def search_book(author=None, title=None):
        """
        Search for books by author and/or title with partial matches.
        If both author and title are None, return all books.
        """
        query = "SELECT * FROM books"
        params = []
        filters = []
        
        if author:
            filters.append("author LIKE ?")
            params.append(f"%{author}%") 
        if title:
            filters.append("title LIKE ?")
            params.append(f"%{title}%")  # Partial match
        
        if filters:
            query += " WHERE " + " AND ".join(filters)
        
        rows = execute_query(query, tuple(params), fetch=True)
        
        return [BookModel(row["id"], row["title"], row["author"], row["year"], row["genre"], row["borrowed_by"], row["ISBN"]) for row in rows]
  
  
    @staticmethod
    def get_paginated_books(page, per_page):
        """
        Fetch books with pagination.
        Args:
            page (int): Page number (1-based).
            per_page (int): Number of items per page.
        Returns:
            List of book models for the requested page.
        """
  
        offset = (page - 1) * per_page

       
        query = "SELECT * FROM books LIMIT ? OFFSET ?"
        rows = execute_query(query, (per_page, offset), fetch=True)
        
        
        return [BookModel(row["id"], row["title"], row["author"], row["year"], row["genre"], row["borrowed_by"], row["ISBN"]) for row in rows]