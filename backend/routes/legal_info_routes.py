# backend/routes/legal_info_routes.py

from flask import Blueprint, jsonify
from models import LegalInfo

legal_info_bp = Blueprint('legal_info_bp', __name__)

@legal_info_bp.route('/', methods=['GET'])
def get_all_legal_info():
    legal_infos = LegalInfo.query.all()
    return jsonify([info.to_dict() for info in legal_infos]), 200

@legal_info_bp.route('/<category>', methods=['GET'])
def get_legal_info_by_category(category):
    info = LegalInfo.query.filter_by(category=category).first()
    if info:
        return jsonify(info.to_dict()), 200
    else:
        return jsonify({'message': 'Category not found.'}), 404
