# backend/app.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # Import the configuration class

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from the Config class
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import and register the blueprint from routes.legal_info_routes
from routes.legal_info_routes import legal_info_bp
app.register_blueprint(legal_info_bp)

# Example main route
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/render')
def render():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
