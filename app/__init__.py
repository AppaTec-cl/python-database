from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pymysql
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{CLOUD_SQL_USER}:{CLOUD_SQL_PASSWORD}@127.0.0.1:3306/{CLOUD_SQL_DATABASE}'.format(**os.environ)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)

    from .auth.login import auth_blueprint
    from .main.submit_form import main_blueprint
    from .main.sumbit_contract import contract_blueprint
    from .main.contract_operations import contract_ops
    from .routes.contract_routes import contract_routes

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(contract_blueprint)
    app.register_blueprint(contract_ops)
    app.register_blueprint(contract_routes)

    @app.route('/')
    def index():
        return "Hello, AppaTec!"

    return app
