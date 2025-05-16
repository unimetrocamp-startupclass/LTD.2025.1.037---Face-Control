from flask import Blueprint, request, jsonify
from app.controllers.image_handler import ImageHandler
import os

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem enviada.'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'Nome de arquivo vazio.'}), 400

    handler = ImageHandler()
    saved_path = handler.save_image(image)

    return jsonify({'message': 'Imagem salva com sucesso.', 'path': saved_path}), 200
