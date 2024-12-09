class book_queries :
    create_books = """
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER,
                    genre TEXT,
                    borrowed_by TEXT , 
                    ISBN TEXT
                )
            """
    add_books =      "INSERT INTO books (title, author, year, genre , borrowed_by , ISBN) VALUES (?, ?, ?, ? , ? , ?)"
    
    get_all_books = "select * from books"    
    
    update_books = """
                UPDATE books
                SET title = ?, author = ?, year = ?, genre = ?, borrowed_by = ?, ISBN = ?
                WHERE id = ?
            """
            
    book_by_id = "select * from books where id = ?"
    
    delete_book = "delete from books where id = ?"