from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    description: str
    category: str


books = [
    {
        "id": 1,
        "title": "The sun Also Rises",
        "author": "Ernest Hemingway",
        "category": "fiction",
    },
    {
        "id": 2,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "fiction",
    },
    {
        "id": 3,
        "title": "Skin in the Game",
        "author": "Nassem Talib",
        "category": "non-fiction"
    }
]


@app.get("/api")
def hello_world():
    return {"msg": "hello world"}
    # return books


@app.get("/book/{path_param}")
def get_path(path_param: str):
    return {"msg": path_param}


@app.get("/books/")
def get_query(title: str):
    return {"msg": title}


@app.get("/books/{book_id}")
async def read_item(book_id: int):
    return books[book_id - 1]


@app.get("/both/{path_param}")
def get_both(title: str, path_param: str):
    return {"msg": title + ' ' + path_param}


@app.post("/book")
def post_book(new_book: Book):
    books.append(new_book.dict())
    print(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_item(book_id: int, book: Book):
    books[book_id - 1] = book
    return books[book_id - 1]


@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    books.pop(book_id - 1)
    return books