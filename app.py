import sqlite3

from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


def get_db_connection():
    connection = sqlite3.connect("birthdays.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        connection = get_db_connection()
        connection.execute(
            "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
            (name, month, day)
        )
        connection.commit()
        connection.close()

        return redirect("/")

    else:
        connection = get_db_connection()
        rows = connection.execute("SELECT * FROM birthdays").fetchall()
        connection.close()

        return render_template("index.html", rows=rows)