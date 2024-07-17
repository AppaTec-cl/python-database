
from flask import Blueprint, jsonify, request
from ..models.contract import Contract
from .. import db

contract_ops = Blueprint('contract_ops', __name__)

@contract_ops.route('/update_contract/<contract_id>', methods=['POST'])
def update_contract(contract_id):
    try:
        contract = Contract.query.filter_by(id_contrato=contract_id).first()
        if contract:
            contract.estado = "Revisado"
            contract.revision_gerente = 1
            db.session.commit()
            return jsonify({"message": "Contrato actualizado exitosamente"}), 200
        else:
            return jsonify({"error": "Contrato no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# contract_operations.py

@contract_ops.route('/reject_contract/<contract_id>', methods=['POST'])
def reject_contract(contract_id):
    comentario = request.json.get('comentario', '')  # Obtener el comentario del request
    try:
        contract = Contract.query.filter_by(id_contrato=contract_id).first()
        if contract:
            contract.estado = "Revisado"
            contract.revision_gerente = 0
            contract.comentario = comentario  # Establecer el comentario del gerente
            db.session.commit()
            return jsonify({"message": "Contrato rechazado exitosamente"}), 200
        else:
            return jsonify({"error": "Contrato no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
