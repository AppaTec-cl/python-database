from .. import db
from sqlalchemy import Column, String, ForeignKey, Date

class CreationRecord(db.Model):
    __tablename__ = 'CREA'

    id_contrato = Column(String(6), ForeignKey('CONTRATO.id_contrato'), primary_key=True)
    id_usuario = Column(String(6), ForeignKey('USUARIO.id_usuario'), primary_key=True)
    fecha_creacion = Column(Date, default=db.func.current_date())

    def __init__(self, id_contrato, id_usuario):
        self.id_contrato = id_contrato
        self.id_usuario = id_usuario

    def to_dict(self):
        return {
            "id_contrato": self.id_contrato,
            "id_usuario": self.id_usuario,
            "fecha_creacion": self.fecha_creacion.isoformat(),
        }
