from flask import Blueprint, jsonify
from ..models.contract import Contract
from ..models.content_contract import Contenido_Contrato
from .. import db

contract_by_rut = Blueprint('contract_by_rut', __name__)

@contract_by_rut.route('/get_contract_by_rut/<rut>', methods=['GET'])
def get_contract_by_rut(rut):
    try:
        contract = db.session.query(
            Contract,
            Contenido_Contrato.nombres,
            Contenido_Contrato.apellidos,
            Contenido_Contrato.direccion,
            Contenido_Contrato.estado_civil,
            Contenido_Contrato.fecha_nacimiento,
            Contenido_Contrato.rut,
            Contenido_Contrato.mail,
            Contenido_Contrato.nacionalidad,
            Contenido_Contrato.sistema_salud,
            Contenido_Contrato.afp,
            Contenido_Contrato.nombre_empleador,
            Contenido_Contrato.rut_empleador,
            Contenido_Contrato.cargo,
            Contenido_Contrato.fecha_inicio,
            Contenido_Contrato.fecha_final,
            Contenido_Contrato.indefinido,
            Contenido_Contrato.sueldo_base,
            Contenido_Contrato.asignacio_colacion,
            Contenido_Contrato.bono_asistencia
        ).join(Contenido_Contrato, Contenido_Contrato.id_contrato == Contract.id_contrato)\
         .filter(Contenido_Contrato.rut == rut).first()

        if contract:
            return jsonify({
                'id': contract.Contract.id_contrato,
                'estado': contract.Contract.estado,
                'contrato': contract.Contract.contrato,
                'comentario': contract.Contract.comentario,
                'revision_gerente': contract.Contract.revision_gerente,
                'revision_gerente_general': contract.Contract.revision_gerente_general,
                'nombres': contract.nombres,
                'apellidos': contract.apellidos,
                'direccion': contract.direccion,
                'estado_civil': contract.estado_civil,
                'fecha_nacimiento': contract.fecha_nacimiento,
                'rut': contract.rut,
                'mail': contract.mail,
                'nacionalidad': contract.nacionalidad,
                'sistema_salud': contract.sistema_salud,
                'afp': contract.afp,
                'nombre_empleador': contract.nombre_empleador,
                'rut_empleador': contract.rut_empleador,
                'cargo': contract.cargo,
                'fecha_inicio': contract.fecha_inicio,
                'fecha_final': contract.fecha_final,
                'indefinido': contract.indefinido,
                'sueldo_base': contract.sueldo_base,
                'asignacio_colacion': contract.asignacio_colacion,
                'bono_asistencia': contract.bono_asistencia
            }), 200
        else:
            return jsonify({"message": "No se encontró el contrato con ese RUT"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
