from flask import Blueprint, render_template, request, redirect, url_for, session
from models import add_user, validate_user

auth = Blueprint('auth', __name__)

# database 
users = {}

# Register route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if username in users:
            return "<div class='container mt-5 text-center'><p class='p-3 text-danger'>Username already exists. Try another one.</p><a href='/auth/register' class='btn btn-secondary mt-3'>Back</a></div>"
        
        # Store the user 
        users[username] = password
        return redirect('/auth/login')

    return '''
    <html>
    <head>
        <title>Register</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="bg-light">
        <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
            <form method="post" class="bg-white p-5 rounded shadow-sm" style="width: 100%; max-width: 500px;">
                <h4 class="mb-4 text-center">Register</h4>
                <div class="mb-3">
                    <input type="text" name="username" class="form-control" placeholder="Username" required>
                </div>
                <div class="mb-3">
                    <input type="password" name="password" class="form-control" placeholder="Password" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Register</button>
                <div class="mt-3 text-center">
                    <a href="/auth/login">Already have an account? Login</a>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate username and password
        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/')
        else:
            return "<div class='container mt-5 text-center'><p class='p-3 text-danger'>Invalid credentials. Try again.</p><a href='/auth/login' class='btn btn-secondary mt-3'>Back</a></div>"

    return '''
    <html>
    <head>
        <title>Login</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="bg-light">
        <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
            <form method="post" class="bg-white p-5 rounded shadow-sm" style="width: 100%; max-width: 500px;">
                <h4 class="mb-4 text-center">Login</h4>
                <div class="mb-3">
                    <input type="text" name="username" class="form-control" placeholder="Username" required>
                </div>
                <div class="mb-3">
                    <input type="password" name="password" class="form-control" placeholder="Password" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Login</button>
                <div class="mt-3 text-center">
                    <a href="/auth/register">Don't have an account? Register</a>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''

# Logout route
@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/auth/login')
