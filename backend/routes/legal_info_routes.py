from flask import Blueprint

# Create a Blueprint for legal information routes
legal_info_bp = Blueprint('legal_info', __name__)

# Define a route under the blueprint
@legal_info_bp.route('/legal-info')
def legal_info():
    return "This is the legal information page."

# You can add more routes to handle different legal information logic here
