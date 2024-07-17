import string

from .. import db
from sqlalchemy import Column, String, ForeignKey, Numeric
import random

class Contenido_Contrato(db.Model):
    __tablename__ = 'CONTENIDO_CONTRATO'

    id_cc = Column(String(6), primary_key=True)
    id_contrato = Column(String(6), ForeignKey('CONTRATO.id_contrato'), nullable=False)
    nombres = Column(String(50))
    apellidos = Column(String(50))
    direccion = Column(String(100))
    estado_civil = Column(String(20))
    fecha_nacimiento = Column(String(50))
    rut = Column(String(10))
    mail = Column(String(100))
    nacionalidad = Column(String(30))
    sistema_salud = Column(String(10))
    afp = Column(String(30))
    nombre_empleador = Column(String(100))
    rut_empleador = Column(String(10))
    cargo = Column(String(50))
    fecha_inicio = Column(String(50))
    fecha_final = Column(String(50))
    indefinido = Column(Numeric(1), nullable=False, default='0')
    sueldo_base = Column(Numeric(10, 0))
    asignacio_colacion = Column(Numeric(10, 0))
    bono_asistencia = Column(Numeric(10, 0))

    def __init__(self, **kwargs):
        super(Contenido_Contrato, self).__init__(**kwargs)
        self.id_cc = self.generate_unique_id()

    @staticmethod
    def generate_unique_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def to_dict(self):
        return {
            "id_cc": self.id_cc,
            "id_contrato": self.id_contrato,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "direccion": self.direccion,
            "estado_civil": self.estado_civil,
            "fecha_nacimiento": self.fecha_nacimiento,
            "rut": self.rut,
            "mail": self.mail,
            "nacionalidad": self.nacionalidad,
            "sistema_salud": self.sistema_salud,
            "afp": self.afp,
            "nombre_empleador": self.nombre_empleador,
            "rut_empleador": self.rut_empleador,
            "cargo": self.cargo,
            "fecha_inicio": self.fecha_inicio,
            "fecha_final": self.fecha_final,
            "indefinido": self.indefinido,
            "sueldo_base": float(self.sueldo_base) if self.sueldo_base is not None else None,
            "asignacio_colacion": float(self.asignacio_colacion) if self.asignacio_colacion is not None else None,
            "bono_asistencia": float(self.bono_asistencia) if self.bono_asistencia is not None else None
        }
