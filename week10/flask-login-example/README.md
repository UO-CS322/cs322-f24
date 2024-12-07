# Flask-login example

This example includes the following:

1. User login functionality.
2. A protected route that requires the user to be logged in.
3. Ability to log out.

### Minimal Flask Application Setup

#### Project **Structure**

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

    def get_id(self):
        return self.username  # Return the username as ID


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

In the minimal Flask application example provided, the username and password are stored in a simple Python dictionary within the `app.py` file. This dictionary serves as a mock user database for demonstration purposes. Here’s how it works:

### User Data Storage

Inside `app.py`, you have the following code snippet:

```python
# Dummy user data for demonstration (replace this with a proper user authentication system)
users = {
    "testuser": {
        "password": "testpassword"  # In a real app, use hashed passwords
    }
}
```

### Explanation

- **Dictionary Structure**: The `users` dictionary holds usernames as keys and a nested dictionary containing passwords as values. For instance, the username `testuser` has a password of `testpassword`.
- **In-Memory Storage**: This approach uses in-memory storage, which means that users and their passwords are not persisted across application restarts. The data is only stored in the application’s memory while it is running.
- **Security Concerns**:
    - **Not Secure for Production**: Hardcoding usernames and passwords like this is not secure, especially as it exposes password data directly. In a real application, you should never store plain text passwords.
    - **Use Hashed Passwords**: For real-world applications, it's a best practice to hash passwords using libraries like `bcrypt`, `werkzeug.security`, or others before storing them. This way, even if the database is compromised, passwords remain safe.

### Improving User Storage for Production

If you want to enhance the application and manage users more securely and effectively, consider the following options:

1. **Use a Database**: Store user credentials in a database (like MongoDB, PostgreSQL, MySQL, etc.). This allows persistence and better management of user accounts.
2. **Password Hashing**: Use libraries to hash passwords before storing them. Here’s a brief example of how to use `werkzeug.security` to hash and check passwords:

   ```python
   from werkzeug.security import generate_password_hash, check_password_hash

   # Hash a password
   hashed_password = generate_password_hash('testpassword')

   # Store in users dictionary
   users = {
       "testuser": {
           "password": hashed_password  # Store the hashed password
       }
   }

   # To verify during login
   if username in users and check_password_hash(users[username]['password'], password):
       # Password is correct, log the user in
   ```

By implementing these best practices, you'll significantly enhance the security of your application and protect user data effectively.

## Other details

### What is `UserMixin`?

`UserMixin` is a class provided by the Flask-Login extension, which is used to simplify the implementation of user authentication in Flask applications. It provides default implementations for several methods required by Flask-Login, making it easier to manage user sessions and authentication.

### Key Features of `UserMixin`

Here are some of the key attributes and methods that `UserMixin` provides:

1. **`is_authenticated`**: This property returns `True` if the user is authenticated. This is typically used to check whether the user has successfully logged in.
2. **`is_active`**: This property returns `True` for active users. You can customize this to check if the user account is active or banned.
3. **`is_anonymous`**: This property returns `True` for anonymous (not logged-in) users. This can be used to differentiate between authenticated users and visitors.
4. **`get_id()`**: This method should return a unique identifier for the user, typically the user's username or user ID. This is used by Flask-Login to manage user sessions.

### Example of Using `UserMixin`

Here's how you might implement a user class that inherits from `UserMixin`:

```python
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username  # Return the username as the unique identifierg
```
