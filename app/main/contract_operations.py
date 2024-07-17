
from flask import Blueprint, jsonify, request
from ..models.contract import Contract
from ..models.user import User
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

@contract_ops.route('/update_contract_gerent/<contract_id>', methods=['POST'])
def update_contract_gerent(contract_id):
    try:
        contract = Contract.query.filter_by(id_contrato=contract_id).first()
        if contract:
            contract.estado = "Revisado Gerente"
            contract.revision_gerente_general = 1
            db.session.commit()
            return jsonify({"message": "Contrato actualizado exitosamente"}), 200
        else:
            return jsonify({"error": "Contrato no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@contract_ops.route('/reject_contract_gerent/<contract_id>', methods=['POST'])
def reject_contract_gerent(contract_id):
    comentario = request.json.get('comentario', '')
    try:
        contract = Contract.query.filter_by(id_contrato=contract_id).first()
        if contract:
            contract.estado = "Revisado Gerente"
            contract.revision_gerente_general = 0
            contract.comentario = comentario
            db.session.commit()
            return jsonify({"message": "Contrato rechazado exitosamente"}), 200
        else:
            return jsonify({"error": "Contrato no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@contract_ops.route('/sign', methods=['POST'])
def sign():
    data = request.get_json()
    id_usuario = data['id_usuario']
    user = User.query.filter_by(id_usuario=id_usuario).first()
    if user:
        return jsonify({
            'firma': user.firma,
        }), 200

@contract_ops.route('/link_sign/<contract_id>', methods=['POST'])
def sign_contract(contract_id):
    link_contrato = request.json.get('contrato', '')
    try:
        contract = Contract.query.filter_by(id_contrato=contract_id).first()
        if contract:
            contract.estado = "Revisado Gerente"
            contract.revision_gerente_general = 1
            contract.contrato = link_contrato
            db.session.commit()
            return jsonify({"message": "Contrato firmado exitosamente"}), 200
        else:
            return jsonify({"error": "Contrato no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500