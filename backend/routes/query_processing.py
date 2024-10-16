# backend/routes/query_processing.py

from flask import Blueprint, request, jsonify
from services.nlp_service import process_query
from models import LegalInfo

query_processing_bp = Blueprint('query_processing_bp', __name__)

@query_processing_bp.route('/', methods=['POST'])
def process_user_query():
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({'error': 'No query provided.'}), 400

    # Use NLP service to extract keywords
    keywords = process_query(user_query)
    
    # Search for matching legal info
    results = []
    for keyword in keywords:
        info = LegalInfo.query.filter(LegalInfo.category.ilike(f'%{keyword}%')).first()
        if info:
            results.append(info.to_dict())

    if results:
        return jsonify({'response': results}), 200
    else:
        return jsonify({'response': 'Sorry, no relevant legal information found.'}), 404
