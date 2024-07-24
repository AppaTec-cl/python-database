from flask import Blueprint, request, jsonify
from flask_mail import Message, Mail
from itsdangerous import URLSafeTimedSerializer
from ..models.user import User
from .. import db
import bcrypt
import base64
import os

recover_password_blueprint = Blueprint('recover_password', __name__)

serializer = URLSafeTimedSerializer('d672ba239be9fe35fe94f36e99717616af745a9c994b08372de4abd262b06228')  # Usa tu propia clave secreta

recovery_mail = Mail()
def setup_recovery_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.zoho.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = os.environ.get('RECOVERY_EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('RECOVERY_EMAIL_PASS')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('RECOVERY_EMAIL_USER')
    recovery_mail.init_app(app)
setup_recovery_mail(create_app())

@recover_password_blueprint.route('/request_reset', methods=['POST'])
def request_reset():
    data = request.get_json()
    rut = data.get('rut')
    user = User.query.filter_by(rut=rut).first()

    if user:
        token = serializer.dumps(user.rut, salt='password-reset-salt')

        subject = "Recuperación de Contraseña"
        body = (
            f"Estimado {user.nombres},\n\n"
            f"Ha solicitado restablecer su contraseña. Use el siguiente token para restablecer su contraseña:\n"
            f"{token}\n\n"
            "Si no solicitó este cambio, puede ignorar este correo.\n\n"
            "Saludos cordiales,\n"
            "El Equipo de AppaTec"
        )

        msg = Message(subject, recipients=[user.mail])
        msg.body = body
        recovery_mail.send(msg)

        return jsonify({"message": "Se ha enviado un correo electrónico con instrucciones para restablecer su contraseña"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@recover_password_blueprint.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    try:
        rut = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # Token válido por 1 hora
    except:
        return jsonify({"error": "Token inválido o expirado"}), 400

    data = request.get_json()
    new_password = data.get('new_password')
    user = User.query.filter_by(rut=rut).first()

    if user:
        user.password = hash_password_bcrypt(new_password)
        db.session.commit()
        return jsonify({"message": "Contraseña actualizada exitosamente"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

def hash_password_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return base64.b64encode(hashed).decode('utf-8')
