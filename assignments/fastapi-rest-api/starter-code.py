from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books = []


# 1. Add a route for GET /
# 2. Add routes for GET /books and POST /books
# 3. Add routes for GET /books/{book_id}, PUT /books/{book_id},
#    and DELETE /books/{book_id}
