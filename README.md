📚 BookAppstore Using FASTAPI and Python
* BookAppstore is a lightweight CRUD API built with FastAPI that allows you to manage a simple digital bookstore. It uses a JSON file as the data storage backend, making it ideal for small-scale or educational purposes.

🚀 Features
* Create, Read, Update, and Delete (CRUD) books
* Fast and asynchronous API powered by FastAPI
* Simple JSON file as database (no external DB needed)
* Easily extendable and beginner-friendly

🛠 Tech Stack
* FastAPI – for building high-performance APIs
* Python 3.9+
* JSON – for lightweight, file-based storage

▶️ Running the App
* uvicorn main:app --reload 
        or
* Python main.py
* Open your browser and Visit: http://127.0.0.1:8000/docs to access the interactive Swagger UI.


🧪 Example Book Format (JSON)

{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "category": 10.99
}

📚 API Endpoints

1. Get all books

Endpoint: GET /books/
Description: Returns a list of all books in the store.
Response example:

[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 10.99
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "price": 8.99
  }
]

2. Get a book by ID
Endpoint: GET /books/{book_id}
Description: Retrieves a single book by its ID.
Response example:
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 10.99
}
-> Error: Returns 404 if the book is not found.

3. Create a new book

Endpoint: POST /books/
Description: Adds a new book to the store.
Request body example:
{
  "title": "Brave New World",
  "author": "Aldous Huxley",
  "price": 9.99
} 
-> Response: Returns the created book with an assigned id

4. Update a book

Endpoint: PUT /books/{book_id}
Description: Updates an existing book by ID.
Request body example:
{
  "title": "Brave New World Revisited",
  "author": "Aldous Huxley",
  "price": 11.50
}
-> Response: Returns the updated book.
-> Error: Returns 404 if the book is not found.

5. Delete a book

Endpoint: DELETE /books/{book_id}
Description: Deletes a book by its ID.
Response: Returns a success message.
Error: Returns 404 if the book is not found.
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 10.99
}