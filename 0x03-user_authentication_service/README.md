# 0x03. User Authentication Service

## Description

This project, part of the ALX Software Engineering curriculum, involves implementing a user authentication service using Flask. While in industry it's recommended to use pre-built modules or frameworks for authentication, such as Flask-User, this project will walk through the process of creating an authentication system from scratch to understand the underlying mechanisms.

## Learning Objectives

By the end of this project, you should be able to:

- Declare API routes in a Flask app
- Get and set cookies
- Retrieve request form data
- Return various HTTP status codes

## Resources

Read or watch the following resources to aid your understanding:

- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
- [Requests module](https://docs.python-requests.org/en/latest/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Requirements

- **Editors Allowed:** vi, vim, emacs
- **Interpreter/Compiler:** Python 3.7 on Ubuntu 18.04 LTS
- **Code Style:** Follow pycodestyle (version 2.5)
- **SQLAlchemy:** Use version 1.3.x
- **Documentation:** All modules, classes, and functions must have comprehensive documentation
- **Annotations:** All functions should be type annotated
- **Interaction:** The Flask app should only interact with the Auth class, not the database (DB) directly

## Mandatory File

- A `README.md` file at the root of the project folder

## Additional Requirements

- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have a documentation string that can be verified using:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
