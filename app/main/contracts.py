from flask import Blueprint, request, jsonify
from google.cloud import storage
import os
from .models import db, Contrato  # Asegúrate de tener un modelo Contrato adecuado

contracts_blueprint = Blueprint('contracts', __name__)

@contracts_blueprint.route('/upload', methods=['POST'])
def upload_contract():
    file = request.files['file']
    file_name = file.filename
    blob_url = upload_to_gcs(file, file_name)
    new_contract = Contrato(nombre=file_name, ruta_archivo=blob_url)
    db.session.add(new_contract)
    db.session.commit()
    return jsonify({'url': blob_url}), 201

def upload_to_gcs(file, file_name):
    client = storage.Client()
    bucket = client.bucket(os.getenv('GCS_BUCKET_NAME'))
    blob = bucket.blob(file_name)
    blob.upload_from_file(file)
    return blob.public_url

@contracts_blueprint.route('/contracts', methods=['GET'])
def list_contracts():
    contracts = Contrato.query.all()
    return jsonify([{'nombre': c.nombre, 'url': c.ruta_archivo} for c in contracts]), 200
