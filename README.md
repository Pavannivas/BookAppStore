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