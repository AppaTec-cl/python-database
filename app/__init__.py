from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
import pymysql
import os

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{CLOUD_SQL_USER}:{CLOUD_SQL_PASSWORD}@127.0.0.1:3306/{CLOUD_SQL_DATABASE}'.format(**os.environ)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Configuración de Flask-Mail para Zoho
    app.config['MAIL_SERVER'] = 'smtp.zoho.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = os.environ.get('ZOHO_EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('ZOHO_EMAIL_PASS')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('ZOHO_EMAIL_USER')

    # Configuración específica para recuperación de contraseñas
    app.config['RECOVERY_MAIL_SERVER'] = 'smtp.zoho.com'
    app.config['RECOVERY_MAIL_PORT'] = 587
    app.config['RECOVERY_MAIL_USE_TLS'] = True
    app.config['RECOVERY_MAIL_USE_SSL'] = False
    app.config['RECOVERY_MAIL_USERNAME'] = os.environ.get('RECOVERY_EMAIL_USER')
    app.config['RECOVERY_MAIL_PASSWORD'] = os.environ.get('RECOVERY_EMAIL_PASS')
    app.config['RECOVERY_MAIL_DEFAULT_SENDER'] = os.environ.get('RECOVERY_EMAIL_USER')
    
    # Inicialización de extensiones
    CORS(app)
    db.init_app(app)
    mail.init_app(app)

    from .auth.login import auth_blueprint
    from .main.submit_form import main_blueprint
    from .main.submit_contract import contract_blueprint
    from .main.contract_operations import contract_ops
    from .routes.contract_routes import contract_routes
    from .routes.contract_all import contract_all_routes
    from .main.recover_password import recover_password_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(contract_blueprint)
    app.register_blueprint(contract_ops)
    app.register_blueprint(contract_routes)
    app.register_blueprint(contract_all_routes)
    app.register_blueprint(recover_password_blueprint)


    @app.route('/')
    def index():
        return "Hello, AppaTec!"

    return app
