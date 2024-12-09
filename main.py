from flask import Flask
from routes.books import books_bp
from routes.user import users_bp
from controllers.books_controller import BooksController
from controllers.users_controller import user_controller

app = Flask(__name__)

BooksController.create_books_table()

user_controller.create_table()




app.register_blueprint(books_bp)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    
    app.run(debug=True)
