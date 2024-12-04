from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a random secret key

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user data for demonstration (replace this with a proper user authentication system)
users = {
    "testuser": {"password": "testpassword"}  # In a real app, use hashed passwords
}


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username  # Return the username as ID


@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)
    return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            user = User(username)
            login_user(user)
            flash("Logged in successfully.")
            return redirect(url_for("protected"))
        flash("Invalid username or password.")
    return render_template("login.html")


@app.route("/protected")
@login_required
def protected():
    return f"Hello, {current_user.username}! You are logged in."


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5008)
