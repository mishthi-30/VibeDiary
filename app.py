from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "vibediary-secret-key"

DATABASE = "vibediary.db"


# ---------------- DATABASE ----------------

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CREATE ACCOUNT ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Username and password are required."

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()

        try:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()

        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists. Please choose another username."

        conn.close()

        session["username"] = username

        return redirect(url_for("dashboard"))

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(user["password"], password):

            session["username"] = username

            return redirect(url_for("dashboard"))

        return "Invalid username or password."


    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# ---------------- START APPLICATION ----------------

if __name__ == "__main__":

    init_db()

    app.run(debug=True)