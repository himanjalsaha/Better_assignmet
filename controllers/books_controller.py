# controllers/books_controller.py
from flask import request, jsonify
from services.book import Books_services

class BooksController:
    
    @staticmethod
    def create_books_table():
        Books_services.create_books_table()

    @staticmethod
    def add_book():
        data = request.json
        title = data.get("title")
        author = data.get("author")
        year = data.get("year")
        genre = data.get("genre")
        borrowed_by = data.get("borrowed_by")
        ISBN = data.get("ISBN")

        if not title or not author:
            return jsonify({"error": "Title and author are required"}), 400

        Books_services.add_book(title, author, year, genre, borrowed_by, ISBN)
        return jsonify({"message": "Book added successfully"}), 201

    @staticmethod
    def get_books():
        page = int(request.args.get('page', 1))  
        per_page = int(request.args.get('per_page', 10))  
        books = Books_services.get_paginated_books(page , per_page)
        
        return jsonify([book.to_dict() for book in books]), 200

    @staticmethod
    def update_book(book_id):
        data = request.json
        title = data.get("title")
        author = data.get("author")
        year = data.get("year")
        genre = data.get("genre")
        borrowed_by = data.get("borrowed_by")
        ISBN = data.get("ISBN")

        if not title or not author:
            return jsonify({"error": "Title and author are required"}), 400

        Books_services.update_book(book_id, title, author, year, genre, borrowed_by, ISBN)
        return jsonify({"message": "Book updated successfully"}), 200

    @staticmethod
    def book_by_id(book_id):
        book = Books_services.get_book_by_id(book_id)
        if book:
            return jsonify(book.to_dict()), 200
        return jsonify({"error": f'Book not found {book_id}'}), 404
        
        
    @staticmethod
    def delete_book(book_id):
        deleted = Books_services.delete_book(book_id)
        if deleted:
            return jsonify({"message":"successfully deleted"}) , 201 
        return jsonify({"error":"unable to delete"})  , 400
        
     
    @staticmethod
    def search_books():
        author = request.args.get("author")
        title = request.args.get("title")

        books = Books_services.search_book(author=author, title=title)
        
        if books:
            return jsonify([book.to_dict() for book in books]), 200
        return jsonify({"message": "No books found matching the criteria"}), 404

                
            