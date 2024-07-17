from flask import Blueprint, jsonify
from ..models.contract import Contract
from ..models.content_contract import Contenido_Contrato
from .. import db

contract_routes = Blueprint('contract_routes', __name__)

@contract_routes.route('/get_contracts/<status>', methods=['GET'])
def get_contracts(status):
    try:
        contracts = db.session.query(
            Contract,
            Contenido_Contrato.nombres,
            Contenido_Contrato.apellidos,
            # Añadir más campos de Contenido_Contrato según sea necesario
        ).join(Contenido_Contrato, Contenido_Contrato.id_contrato == Contract.id_contrato)\
         .filter(Contract.estado == status).all()

        return jsonify([
            {
                'id': contract.id_contrato,
                'estado': contract.estado,
                'fecha_inicio': contract.fecha_inicio,
                'fecha_expiracion': contract.fecha_expiracion,
                'contrato': contract.contrato,
                'comentario': contract.comentario,
                'nombres': contenido_nombres,  # Ejemplo de campo aplanado
                'apellidos': contenido_apellidos,  # Otro ejemplo de campo aplanado
            } for contract, contenido_nombres, contenido_apellidos in contracts
        ]), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
