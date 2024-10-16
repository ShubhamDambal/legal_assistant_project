# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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

if __name__ == '__main__':
    app.run(debug=True)
