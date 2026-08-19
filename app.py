from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "vibediary-secret-key"

# SQLite database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vibediary.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =========================
# User Model
# =========================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# =========================
# Create Database
# =========================

with app.app_context():
    db.create_all()


# =========================
# Home Page
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# Register
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return "Username already exists. Please choose another."

        # Hash password before storing it
        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        session["username"] = username

        return redirect(url_for("dashboard"))

    return render_template("register.html")


# =========================
# Login
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            session["username"] = username

            return redirect(url_for("dashboard"))

        return "Invalid username or password."

    return render_template("login.html")


# =========================
# Dashboard
# =========================

@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )

# =========================
# Create Diary Entry
# =========================

@app.route("/create-entry", methods=["GET", "POST"])
def create_entry():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")
        mood = request.form.get("mood")

        if not title or not content or not mood:
            return "Please fill in all fields."

        new_entry = DiaryEntry(
            username=session["username"],
            title=title,
            content=content,
            mood=mood
        )

        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for("dashboard"))

    return render_template("create_entry.html")

# =========================
# Logout
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# =========================
# Run Application
# =========================

if __name__ == "__main__":
    app.run(debug=True)