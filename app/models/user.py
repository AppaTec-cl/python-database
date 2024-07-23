from .. import db
import bcrypt
import base64
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    __tablename__ = 'USUARIO'
    id_usuario = db.Column(db.String(6), primary_key=True)
    rut = db.Column(db.String(10), nullable=False, unique=True)
    nombres = db.Column(db.String(40), nullable=False)
    apellido_p = db.Column(db.String(20), nullable=False)
    apellido_m = db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    firma = db.Column(db.String(500), nullable=True)

    def check_password(self, password):
        hashed_password_bytes = base64.b64decode(self.password.encode('utf-8'))
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes)
    
    @hybrid_property
    def id(self):
        numeric_part = self.rut.split('-')[0]
        return str(numeric_part[-6:])
    
    @id.setter
    def id(self, rut):
        self.rut = rut

    def __init__(self, rut, nombres, apellido_p, apellido_m, correo_electronico, rol, password, firma, id_usuario=None):
        self.rut = rut
        self.nombres = nombres
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.mail = correo_electronico
        self.rol = rol
        self.password = password
        self.firma = firma
        self.id_usuario = self.id

