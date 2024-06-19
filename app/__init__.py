from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://appa:HolaCarlita03@34.176.56.6/gestor-contrato'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .auth.login import auth_blueprint
    from .main.submit_form import main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app
