from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos usando PyMySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://appa:HolaCarlita03@34.176.56.6/gestor_contratos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de usuario
class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    return "Hello, Flask with MySQL and PyMySQL!"

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')

    # Crear una nueva instancia de User
    new_user = User(nombre=nombre, apellido=apellido, email=email)
    db.session.add(new_user)
    db.session.commit()

    # Imprime los datos recibidos para probar el funcionamiento
    print(f"Nombre: {nombre}, Apellido: {apellido}, Email: {email}")

    response = {
        'message': 'Form data received and saved to database!',
        'data': {
            'nombre': nombre,
            'apellido': apellido,
            'email': email
        }
    }
    return jsonify(response)

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {
            'id': user.id,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'email': user.email
        }
        result.append(user_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
