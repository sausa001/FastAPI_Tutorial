from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

## in-memory storage for books
books = [

    {
        "id": 1, 
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949
     },

    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960
        },

    {
        "id": 3,
        "title": "The Great Gatsby", 
        "author": "F. Scott Fitzgerald",
        "published_year": 1925
    },

    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_year": 1813
 }
# {
#         "id": 5,   
#         "title": "The Catcher in the Rye",
#         "author": "J.D. Salinger",
#         "published_year": 1951 
# }

]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    #return {"error": "Book not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# Add some additional books in above list using post method

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

@app.post("/books")
def add_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

# @app.post("/books")
# def add_book(book: dict):
#     books.append(book)
#     return book 

# Update a book's information using PUT method
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for  index, book in enumerate(books):
        if book["id"] == book_id:
           books[index]["title"] = updated_book.title
           books[index]["author"] = updated_book.author
           books[index]["published_year"] = updated_book.published_year
           #books[index] = updated_book.model_dump()
           return books[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# Delete a book from the collection using DELETE method
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 