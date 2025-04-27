from flask import Flask, session, redirect, url_for, request, jsonify
from auth import auth  # Import the auth blueprint

# Initialize the Flask app
app = Flask(__name__)

# Configure a secret key for session management
app.secret_key = 'your_secret_key'

# Register the auth blueprint
app.register_blueprint(auth, url_prefix='/auth')

# Initialize programs and clients globally 
programs = {}
clients = {}

# Home route 
@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/auth/login')
    
    return '''
    <html>
    <head>
        <title>Health Info System</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="bg-light p-4">
        <div class="container">
            <div class="card shadow-sm p-4">
                <h2 class="mb-4 text-center">Health Information System</h2>
                <div class="list-group">
                    <a href="/create_program" class="list-group-item list-group-item-action">Create Health Program</a>
                    <a href="/register_client" class="list-group-item list-group-item-action">Register New Client</a>
                    <a href="/enroll_client" class="list-group-item list-group-item-action">Enroll Client in Program</a>
                    <a href="/search_client" class="list-group-item list-group-item-action">Search for Client</a>
                    <a href="/view_clients" class="list-group-item list-group-item-action">View All Clients</a>
                    <a href="/auth/logout" class="list-group-item list-group-item-action">Logout</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

# Create Health Program
@app.route('/create_program', methods=['GET', 'POST'])
def create_program():
    if 'user' not in session:
        return redirect('/auth/login')  # Redirect to login if user is not logged in

    if request.method == 'POST':
        name = request.form['program_name']
        programs[name] = {'name': name}
        return f"<div class='container mt-5 text-center'><p class='p-3 text-success'>Program '{name}' created successfully.</p><a href='/' class='btn btn-secondary mt-3'>Back</a></div>"

    return '''
    <html>
    <head>
        <title>Create Health Program</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="bg-light">
        <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
            <form method="post" class="bg-white p-5 rounded shadow-sm" style="width: 100%; max-width: 500px;">
                <h4 class="mb-4 text-center">Create Health Program</h4>
                <div class="mb-3">
                    <input type="text" name="program_name" class="form-control" placeholder="e.g. TB, Malaria" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Create</button>
                <div class="mt-3 text-center">
                    <a href="/">Back to Home</a>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''

# Register Client
@app.route('/register_client', methods=['GET', 'POST'])
def register_client():
    if 'user' not in session:
        return redirect('/auth/login')  # Redirect to login if user is not logged in

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        clients[name] = {'name': name, 'age': age, 'programs': []}
        return f"<div class='container mt-5 text-center'><p class='p-3 text-success'>Client '{name}' registered successfully.</p><a href='/' class='btn btn-secondary mt-3'>Back</a></div>"

    return '''
    <html>
    <head>
        <title>Register Client</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="bg-light">
        <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
            <form method="post" class="bg-white p-5 rounded shadow-sm" style="width: 100%; max-width: 500px;">
                <h4 class="mb-4 text-center">Register New Client</h4>
                <div class="mb-3">
                    <input type="text" name="name" class="form-control" placeholder="Full Name" required>
                </div>
                <div class="mb-3">
                    <input type="number" name="age" class="form-control" placeholder="Age" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Register</button>
                <div class="mt-3 text-center">
                    <a href="/">Back to Home</a>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''

# Enroll Client in Program
@app.route('/enroll_client', methods=['GET', 'POST'])
def enroll_client():
    if 'user' not in session:
        return redirect('/auth/login')  # Redirect to login if user is not logged in

    if request.method == 'POST':
        client_name = request.form['client_name']
        program_name = request.form['program_name']
        if client_name in clients and program_name in programs:
            if program_name not in clients[client_name]['programs']:
                clients[client_name]['programs'].append(program_name)
                return f"<div class='container mt-5 text-center'><p class='p-3 text-success'>{client_name} enrolled in {program_name}.</p><a href='/' class='btn btn-secondary mt-3'>Back</a></div>"
            else:
                return f"<div class='container mt-5 text-center'><p class='p-3 text-warning'>{client_name} is already enrolled in {program_name}.</p><a href='/' class='btn btn-secondary mt-3'>Back</a></div>"
        else:
            return f"<div class='container mt-5 text-center'><p class='p-3 text-danger'>Invalid client or program name.</p><a href='/' class='btn btn-secondary mt-3'>Back</a></div>"

    return '''
    <html>
    <head>
        <title>Enroll Client</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="bg-light">
        <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
            <form method="post" class="bg-white p-5 rounded shadow-sm" style="width: 100%; max-width: 500px;">
                <h4 class="mb-4 text-center">Enroll Client in Program</h4>
                <div class="mb-3">
                    <input type="text" name="client_name" class="form-control" placeholder="Client Name" required>
                </div>
                <div class="mb-3">
                    <input type="text" name="program_name" class="form-control" placeholder="Program Name" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Enroll</button>
                <div class="mt-3 text-center">
                    <a href="/">Back to Home</a>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''

# Search Client
@app.route('/search_client', methods=['GET', 'POST'])
def search_client():
    if 'user' not in session:
        return redirect('/auth/login')  # Redirect to login if user is not logged in

    if request.method == 'POST':
        name = request.form['name']
        if name in clients:
            return redirect(f'/client_profile/{name}')
        else:
            return f"<div class='container mt-5 text-center'><p class='p-3 text-danger'>Client '{name}' not found.</p><a href='/' class='btn btn-secondary mt-3'>Back</a></div>"

    return '''
    <html>
    <head>
        <title>Search Client</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="bg-light">
        <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
            <form method="post" class="bg-white p-5 rounded shadow-sm" style="width: 100%; max-width: 500px;">
                <h4 class="mb-4 text-center">Search for Client</h4>
                <div class="mb-3">
                    <input type="text" name="name" class="form-control" placeholder="Client Name" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Search</button>
                <div class="mt-3 text-center">
                    <a href="/">Back to Home</a>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''

# View Client Profile
@app.route('/client_profile/<name>')
def client_profile(name):
    if 'user' not in session:
        return redirect('/auth/login')  # Redirect to login if user is not logged in

    if name in clients:
        client = clients[name]
        return f'''
        <html>
        <head>
            <title>Client Profile</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        </head>
        <body class="bg-light">
            <div class="container mt-5">
                <div class="card p-4 shadow-sm">
                    <h4 class="text-center mb-4">Client Profile</h4>
                    <p><strong>Name:</strong> {client["name"]}</p>
                    <p><strong>Age:</strong> {client["age"]}</p>
                    <p><strong>Enrolled Programs:</strong> {', '.join(client["programs"]) or "None"}</p>
                    <div class="text-center mt-4">
                        <a href="/" class="btn btn-secondary">Back to Home</a>
                    </div>
                </div>
            </div>
        </body>
        </html>
        '''
    else:
        return f"<div class='container mt-5 text-center'><p class='p-3 text-danger'>Client not found.</p><a href='/' class='btn btn-secondary mt-3'>Back</a></div>"

# Expose Client Profile via API
@app.route('/api/client/<client_id>', methods=['GET'])
def api_get_client(client_id):
    client = clients.get(client_id)
    if client:
        return jsonify(client)
    else:
        return jsonify({"error": "Client not found"}), 404

# View all clients
@app.route('/view_clients')
def view_clients():
    if 'user' not in session:
        return redirect('/auth/login')  # Redirect to login if user is not logged in

    output = "<div class='container mt-5'><h4>Registered Clients</h4><ul class='list-group'>"
    for name in clients:
        output += f"<li class='list-group-item'><a href='/client_profile/{name}'>{name}</a></li>"
    output += "</ul><div class='text-center mt-4'><a href='/' class='btn btn-secondary'>Back to Home</a></div></div>"
    return output

if __name__ == '__main__':
    app.run(debug=True)
