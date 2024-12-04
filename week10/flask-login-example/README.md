# Flask-login example

This example includes the following:

1. User login functionality.
2. A protected route that requires the user to be logged in.
3. Ability to log out.

### Minimal Flask Application Setup

#### Project Structure

```
/flask-login-example
├── app.py
└── requirements.txt
```

#### Step 1: Create `requirements.txt`

Create a `requirements.txt` file to specify your dependencies:

```plaintext
Flask
Flask-Login
```

#### Step 2: Create `app.py`

Now create the main Flask application file `app.py`:

```python
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user data for demonstration (replace this with a proper user authentication system)
users = {
    "testuser": {
        "password": "testpassword"  # In a real app, use hashed passwords
    }
}

class User(UserMixin):
    def __init__(self, username):
        self.username = username

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('protected'))
        flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.username}! You are logged in.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5008)
```

#### Step 3: Create HTML Templates

Create a directory named `templates` next to `app.py`. Inside, create two HTML files:

1. **`index.html`**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Example</title>
</head>
<body>
    <h1>Flask-Login Example</h1>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
          {% for msg in messages %}
            <li>{{ msg }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <a href="{{ url_for('login') }}">Login</a>
</body>
</html>
```

2. **`login.html`**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label><br>
        <input type="text" name="username" required><br>
        <label for="password">Password:</label><br>
        <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
    <p><a href="{{ url_for('index') }}">Back to Home</a></p>
</body>
</html>
```

### Step 4: Running the Application

1. **Install the dependencies**:

   Ensure you have Python installed, and then from your terminal, navigate to the application directory and install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
2. **Run the application**:

   You can run the Flask application using:

   ```bash
   python app.py
   ```
3. **Access the Application**:

   Open your web browser and go to `http://127.0.0.1:5008/`. You will see the home page. Click on "Login" to enter the login page, and use the credentials:

   - Username: `testuser`
   - Password: `testpassword`
