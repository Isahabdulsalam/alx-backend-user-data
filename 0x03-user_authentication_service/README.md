# User Authentication Service

This project contains tasks for learning to create a user authentication service.

## Requirements

- SQLAlchemy 1.3.x
- pycodestyle 2.5
- bcrypt
- python3 3.7

## Tasks To Complete

### User Model
- **File:** `user.py`
- Contains a SQLAlchemy model named `User` for a database table named `users` with the following attributes:
  - `id`: The integer primary key.
  - `email`: A non-nullable string.
  - `hashed_password`: A non-nullable string.
  - `session_id`: A nullable string.
  - `reset_token`: A nullable string.

### Create User
- **File:** `db.py`
- **Class:** `DB`
- **Method:** `add_user(email: str, hashed_password: str) -> User`
- Implements the `add_user` method to save the user to the database without validation.

### Find User
- **File:** `db.py`
- **Method:** `find_user_by(**kwargs) -> User`
- Finds and returns the first user based on arbitrary keyword arguments, raising exceptions when no results are found or wrong query arguments are passed.

### Update User
- **File:** `db.py`
- **Method:** `update_user(user_id: int, **kwargs) -> None`
- Uses `find_user_by` to locate and update the user’s attributes, committing changes to the database.

### Hash Password
- **File:** `auth.py`
- **Method:** `_hash_password(password: str) -> bytes`
- Returns a salted hash of the input password using `bcrypt.hashpw`.

### Register User
- **File:** `auth.py`
- **Class:** `Auth`
- **Method:** `register_user(email: str, password: str) -> User`
- Registers a new user, hashing the password and saving the user to the database. Raises a `ValueError` if the user already exists.

### Basic Flask App
- **File:** `app.py`
- Implements a basic Flask app with a single GET route (`"/"`) that returns a JSON payload `{"message": "Bienvenue"}`.

### Register User Endpoint
- **File:** `app.py`
- **Route:** `POST /users`
- Registers a user and responds with `{"email": "<registered email>", "message": "user created"}` or `{"message": "email already registered"}` with a 400 status code if the user is already registered.

### Credentials Validation
- **File:** `auth.py`
- **Method:** `valid_login(email: str, password: str) -> bool`
- Checks if the user exists and if the password matches using `bcrypt.checkpw`.

### Generate UUIDs
- **File:** `auth.py`
- **Method:** `_generate_uuid() -> str`
- Returns a string representation of a new UUID using the `uuid` module.

### Get Session ID
- **File:** `auth.py`
- **Method:** `create_session(email: str) -> str`
- Generates a new UUID, stores it as the user’s `session_id` in the database, and returns the session ID.

### Log In
- **File:** `app.py`
- **Route:** `POST /sessions`
- Creates a new session for the user, stores the session ID as a cookie, and returns `{"email": "<user email>", "message": "logged in"}` or a 401 status code if the login information is incorrect.

### Find User by Session ID
- **File:** `auth.py`
- **Method:** `get_user_from_session_id(session_id: str) -> User or None`
- Returns the corresponding user based on the session ID or `None` if invalid.

### Destroy Session
- **File:** `auth.py`
- **Method:** `destroy_session(user_id: int) -> None`
- Updates the user’s `session_id` to `None`.

### Log Out
- **File:** `app.py`
- **Route:** `DELETE /sessions`
- Destroys the user’s session and redirects to `GET /`. Returns a 403 status code if the session ID is invalid.

### User Profile
- **File:** `app.py`
- **Route:** `GET /profile`
- Returns `{"email": "<user email>"}` with a 200 status code if the session ID is valid or a 403 status code if invalid.

### Generate Reset Password Token
- **File:** `auth.py`
- **Method:** `get_reset_password_token(email: str) -> str`
- Generates and returns a reset token for the user’s email or raises a `ValueError` if the user does not exist.

### Get Reset Password Token Endpoint
- **File:** `app.py`
- **Route:** `POST /reset_password`
- Returns `{"email": "<user email>", "reset_token": "<reset token>"}` with a 200 status code or a 403 status code if the email is not registered.

### Update Password
- **File:** `auth.py`
- **Method:** `update_password(reset_token: str, password: str) -> None`
- Updates the user’s password using the reset token or raises a `ValueError` if the token is invalid.

### Update Password Endpoint
- **File:** `app.py`
- **Route:** `PUT /reset_password`
- Updates the password and returns `{"email": "<user email>", "message": "Password updated"}` with a 200 status code or a 403 status code if the token is invalid.

### End-to-End Integration Test
- **File:** `main.py`
- Implements integration tests for each endpoint using the `requests` module to validate the response’s expected status code and payload.

### Example Code to Run Integration Tests
```python
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)

Run python3 main.py. If everything is correct, you should see no output.




