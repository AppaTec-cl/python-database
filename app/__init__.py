from flask import Flask
from flasksqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createapp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://appa:AppaTec0306@34.176.56.6/GestorContrato'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
