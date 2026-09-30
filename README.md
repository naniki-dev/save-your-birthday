# Birthdays Web Application

A full-stack web application built with **Python, Flask, SQLite, HTML, and CSS** for managing and displaying friends' birthdays.

## Project Overview

This project is a simple CRUD-style web application that allows users to add and view birthday information through a browser-based interface.

I built the application to strengthen my understanding of **Flask web development, HTTP request handling, HTML forms, server-side rendering, and relational database integration**. The application uses SQLite for persistent data storage and Python's built-in `sqlite3` module to communicate with the database.

The project demonstrates how a web application can connect a frontend interface to backend application logic and a relational database.

## Features

* Add a person's name and birthday
* Store birthday information in a SQLite database
* Display saved birthdays in a table
* Handle HTML form submissions with Flask
* Persist data between application sessions
* Redirect users after submitting a new birthday
* Dynamic HTML rendering using Jinja2
* Parameterized SQL queries for database operations

## Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **HTML5**
* **CSS3**
* **Jinja2**

## Project Structure

```text
birthdays/
│
├── app.py
├── birthdays.db
├── README.md
│
├── static/
│   └── styles.css
│
└── templates/
    └── index.html
```

### File Overview

#### `app.py`

The main Flask application.

It is responsible for:

* Defining application routes
* Handling `GET` and `POST` requests
* Connecting to the SQLite database
* Retrieving birthday records
* Inserting new birthday records
* Rendering the HTML template

#### `birthdays.db`

The SQLite database used to persist birthday information.

The database contains a `birthdays` table with the following columns:

| Column  | Description                         |
| ------- | ----------------------------------- |
| `id`    | Unique identifier for each birthday |
| `name`  | Name of the person                  |
| `month` | Birthday month                      |
| `day`   | Birthday day                        |

#### `templates/index.html`

The main HTML template rendered by Flask.

It contains:

* The birthday submission form
* The table used to display saved birthdays
* Jinja2 template logic for dynamically displaying database records

#### `static/styles.css`

Contains the CSS used to style the application's user interface.

## Prerequisites

Before running the application, make sure you have:

* Python 3 installed
* pip installed
* A web browser

You can check your Python installation with:

```bash
python --version
```

On some systems, you may need:

```bash
python3 --version
```

## Installation

### 1. Clone the Repository

Clone the project to your local machine:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd birthdays
```

### 2. Create a Virtual Environment

Creating a virtual environment keeps the project's Python dependencies isolated from your system environment.

#### Windows

```bash
python -m venv venv
```

#### macOS/Linux

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows Command Prompt

```bash
venv\Scripts\activate
```

#### Windows PowerShell

```bash
venv\Scripts\Activate.ps1
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install Flask

Install Flask using pip:

```bash
pip install Flask
```

If the project contains a `requirements.txt` file, you can install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server from the project directory:

```bash
flask --app app run
```

If successful, the terminal should display something similar to:

```text
* Serving Flask app 'app'
* Running on http://127.0.0.1:5000
```

## Opening the Application

Open your web browser and navigate to:

```text
http://127.0.0.1:5000
```

Alternatively:

```text
http://localhost:5000
```

The Birthdays application should now be accessible in your browser.

## Using the Application

### Viewing Birthdays

When the application loads, it retrieves the birthday records stored in the SQLite database and displays them in a table.

Each entry contains:

* Name
* Birthday month
* Birthday day

### Adding a Birthday

To add a new birthday:

1. Enter the person's name.
2. Enter their birth month.
3. Enter their birth day.
4. Submit the form.

The form sends a `POST` request to the `/` route.

The Flask application then inserts the submitted information into the SQLite database and redirects the user back to the home page.

The new birthday will appear in the table.

## How the Application Works

The application follows a simple request-response flow between the browser, Flask application, and SQLite database.

### GET Request

When the user visits the home page:

```text
Browser
   |
   | GET /
   v
Flask Application
   |
   | SELECT * FROM birthdays
   v
SQLite Database
   |
   | Birthday records
   v
Flask Application
   |
   | Render index.html
   v
Browser
```

The Flask application retrieves the birthday records from the database and passes them to the `index.html` template.

Jinja2 then dynamically generates the table rows based on the database records.

### POST Request

When a user submits the birthday form:

```text
Browser
   |
   | POST /
   | name, month, day
   v
Flask Application
   |
   | INSERT birthday
   v
SQLite Database
   |
   | Save record
   v
Flask Application
   |
   | Redirect /
   v
Browser
```

The submitted information is inserted into the database.

The application then redirects the user to `/`, which triggers a new `GET` request and displays the updated list.

## Database Integration

The application uses Python's built-in `sqlite3` module to communicate with SQLite.

A database connection is created when database operations are required:

```python
def get_db_connection():
    connection = sqlite3.connect("birthdays.db")
    connection.row_factory = sqlite3.Row
    return connection
```

Birthday records are inserted using a parameterized SQL query:

```python
connection.execute(
    "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
    (name, month, day)
)
```

Parameterized queries allow user-provided values to be passed separately from the SQL statement rather than directly constructing SQL with user input.

## Development Mode

Flask's debug mode can be enabled during development:

```bash
flask --app app --debug run
```

This allows Flask to automatically reload the application when changes are made.

The application will be available at:

```text
http://127.0.0.1:5000
```

Debug mode should not be used when deploying an application to production.

## Learning Outcomes

Through this project, I gained practical experience with:

* Building web applications using Flask
* Understanding the request-response cycle
* Handling HTTP `GET` and `POST` requests
* Working with HTML forms
* Rendering dynamic pages with Jinja2
* Connecting a web application to a relational database
* Writing SQL queries
* Using SQLite with Python
* Using parameterized SQL queries
* Managing database connections
* Structuring a small web application
* Persisting application data

## Future Improvements

Potential improvements include:

* Edit existing birthday entries
* Delete birthday entries
* Validate user input
* Add error handling
* Add birthday search functionality
* Sort birthdays chronologically
* Highlight upcoming birthdays
* Add user authentication
* Add automated tests
* Deploy the application to a cloud platform

## Project Background

This project was originally developed as part of the **CS50x** coursework and subsequently adapted to use Python's standard `sqlite3` library rather than the CS50 SQL library.

The implementation was used as an opportunity to apply the concepts independently and better understand how Flask applications interact directly with SQLite databases.

## License

This project is intended for educational and portfolio purposes.
