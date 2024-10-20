# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
import database  # Import the database module

import logging
from logging.handlers import RotatingFileHandler
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database with the app
database.init_app(app)

# Initialize extensions
CORS(app)  # Enable CORS
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes
from routes.legal_info_routes import legal_info_bp
from routes.query_processing import query_processing_bp
from routes.feedback_routes import feedback_bp

# Register blueprints
app.register_blueprint(legal_info_bp, url_prefix='/api/legal_info')
app.register_blueprint(query_processing_bp, url_prefix='/api/query')
app.register_blueprint(feedback_bp, url_prefix='/api/feedback')

# Home route for testing
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Legal Assistant API'})

# New route to fetch sample data from SQLite database
@app.route('/fetch_sample_data', methods=['GET'])
def fetch_sample_data():
    """Fetches data from the SQLite database and returns it as JSON."""
    db = database.get_db()
    cursor = db.execute('SELECT * FROM data_table')  # Replace with your actual table name
    data = cursor.fetchall()
    return jsonify([dict(row) for row in data])

# New route to insert sample data into SQLite database
@app.route('/insert_sample_data', methods=['POST'])
def insert_sample_data():
    """Inserts sample data into the SQLite database."""
    db = database.get_db()
    data = request.get_json()  # Expecting JSON input
    db.execute(
        'INSERT INTO your_table_name (column1, column2) VALUES (?, ?)',  # Replace with your actual table name and columns
        (data['column1'], data['column2'])
    )
    db.commit()
    return jsonify({"message": "Data inserted successfully"}), 201

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description,
    }).data
    response.content_type = "application/json"
    return response

# Error handler for non-HTTP exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle non-HTTP exceptions."""
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/legal_assistant.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Legal Assistant API startup')

if __name__ == '__main__':
    app.run(debug=True)
