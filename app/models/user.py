from .. import db
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(10), nullable=False, unique=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellido_p = db.Column(db.String(50), nullable=False)
    apellido_m = db.Column(db.String(50), nullable=False)
    correo_electronico = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @hybrid_property
    def id(self):
        # Extrae la parte numérica antes del guión en el RUT
        numeric_part = self.rut.split('-')[0]
        # Toma los últimos 6 dígitos
        return int(numeric_part[-6:])
    
    @id.setter
    def id(self, rut):
        self.rut = rut

    def __init__(self, rut, nombres, apellido_p, apellido_m, correo_electronico, rol, password):
        self.rut = rut
        self.nombres = nombres
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.correo_electronico = correo_electronico
        self.rol = rol
        self.password = generate_password_hash(password)
        self.id_usuario = self.id
