# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

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

if __name__ == '__main__':
    app.run(debug=True)
