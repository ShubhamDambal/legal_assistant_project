# backend/routes/feedback_routes.py

from flask import Blueprint, request, jsonify
from models import Feedback
from app import db

feedback_bp = Blueprint('feedback_bp', __name__)

@feedback_bp.route('/', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    feedback_text = data.get('feedback', '')
    
    if not feedback_text:
        return jsonify({'error': 'No feedback provided.'}), 400
    
    new_feedback = Feedback(feedback_text=feedback_text)
    db.session.add(new_feedback)
    db.session.commit()
    
    return jsonify({'message': 'Feedback submitted successfully.'}), 201
