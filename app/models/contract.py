from .. import db
from sqlalchemy import Column, String,Integer, Text
import string
import random

class Contract(db.Model):
    __tablename__ = 'CONTRATO'

    id_contrato = Column(String(6), primary_key=True)
    fecha_inicio = Column(String(50), nullable=False)
    fecha_expiracion = Column(String(50), nullable=True)
    comentario = Column(Text, nullable=True)
    estado = Column(String(15), nullable=False, default='No Revisado')
    revision_gerente = Column(Integer, default=0)
    revision_gerente_general = Column(Integer, default=0)
    ultimo_revisor = Column(String(50), nullable=True)
    fecha_ultima_revision = Column(String(50), nullable=True)
    contrato = Column(Text, nullable=False)  # URL del contrato

    def __init__(self, fecha_inicio, fecha_expiracion, comentario, contrato):
        self.id_contrato = self.generate_unique_id()
        self.fecha_inicio = fecha_inicio
        self.fecha_expiracion = fecha_expiracion
        self.comentario = comentario
        self.estado = 'No Revisado'
        self.revision_gerente = 0
        self.revision_gerente_general = 0
        self.contrato = contrato

    @staticmethod
    def generate_unique_id():
        while True:
            random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            if not Contract.query.filter_by(id_contrato=random_id).first():
                return random_id

    def to_dict(self):
        return {
            "id_contrato": self.id_contrato,
            "fecha_inicio": self.fecha_inicio,
            "fecha_expiracion": self.fecha_expiracion,
            "comentario": self.comentario,
            "estado": self.estado,
            "revision_gerente": self.revision_gerente,
            "revision_gerente_general": self.revision_gerente_general,
            "ultimo_revisor": self.ultimo_revisor,
            "fecha_ultima_revision": self.fecha_ultima_revision,
            "contrato": self.contrato
        }
