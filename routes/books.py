# routes/books_routes.py
from flask import Blueprint
from controllers.books_controller import BooksController
from utils.tokenverification import token_required

books_bp = Blueprint("books", __name__)

# Use the token_required decorator for all routes that require authentication
books_bp.route("/books", methods=["GET"], endpoint="get_books")(token_required(BooksController.get_books))
books_bp.route("/books", methods=["POST"], endpoint="add_book")(token_required(BooksController.add_book))
books_bp.route("/books/<int:book_id>", methods=["PUT"], endpoint="update_book")(token_required(BooksController.update_book))
books_bp.route("/books/<int:book_id>", methods=["DELETE"], endpoint="delete_book")(token_required(BooksController.delete_book))
books_bp.route("/books/<int:book_id>", methods=["GET"], endpoint="get_book_by_id")(token_required(BooksController.book_by_id))
books_bp.route("/books/search", methods=["GET"], endpoint="search_book")(token_required(BooksController.search_books))