from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db
import bcrypt

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.get_json()
    new_user = User(
        rut=data['rut'],
        nombres=data['nombres'],
        apellido_p=data['apellido_p'],
        apellido_m=data['apellido_m'],
        correo_electronico=data['correo_electronico'],
        rol=data['rol'],
        password=hash_password_bcrypt(data['password']),
        firma=data['firma']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuario creado exitosamente', 'user_id': new_user.id_usuario}), 201

def hash_password_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed