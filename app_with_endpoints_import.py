
from flask import Flask, session
from endpoints import init_endpoints

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # This should be more secret in a real application

# Importing and initializing the endpoints
init_endpoints(app)

if __name__ == '__main__':
    app.run(debug=True)
