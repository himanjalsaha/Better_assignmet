from typing import Optional

class BookModel:
    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        year: Optional[int],
        genre: str,
        borrowed_by: Optional[str],
        ISBN: str
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.borrowed_by = borrowed_by
        self.ISBN = ISBN

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": int(self.year) if self.year is not None else None,  
            "genre": self.genre,
            "borrowed_by": self.borrowed_by,
            "ISBN": self.ISBN
        }
