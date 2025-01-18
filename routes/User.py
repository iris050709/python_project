from flask import Blueprint, jsonify

user_bp = Blueprint('users', __name__)

@user_bp.rute('/', methods = ['GET'])
def index():
    return jsonify({})