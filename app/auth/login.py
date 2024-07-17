from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    rut = data['rut']
    password = data['password']
    user = User.query.filter_by(rut=rut).first()
    if user and user.check_password(password):
        return jsonify({
            'rol': user.rol,
            'nombre': user.nombres,
            'id_usuario': user.id_usuario
        }), 200
    else:
        return jsonify({'rol': None}), 401
