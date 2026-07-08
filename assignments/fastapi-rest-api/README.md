# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by defining routes, creating request models, and returning JSON responses for a small book catalog.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a basic FastAPI application and add a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Add a GET route at `/`
- Return a JSON response with a friendly welcome message

### 🛠️ Define a Data Model and Endpoints

#### Description
Create a Pydantic model for books and add endpoints to list and create books.

#### Requirements
Completed program should:

- Define a `Book` model with fields for `id`, `title`, `author`, and `year`
- Add a `GET /books` route that returns a list of books
- Add a `POST /books` route that accepts a new book and stores it

### 🛠️ Add Single-Item Routes and Validation

#### Description
Extend the API so it can retrieve, update, or delete a single book by its ID.

#### Requirements
Completed program should:

- Add a `GET /books/{book_id}` route that returns a book or a 404 error
- Add a `PUT /books/{book_id}` route to update an existing book
- Add a `DELETE /books/{book_id}` route to remove a book
