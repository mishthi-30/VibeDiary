from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "vibediary-secret-key"


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Create Account
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        session["username"] = username

        return redirect(url_for("dashboard"))

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        session["username"] = username

        return redirect(url_for("dashboard"))

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)