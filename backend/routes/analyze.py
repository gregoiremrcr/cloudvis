from flask import Blueprint, request, jsonify
from analysis import analyze_image
from models import insert_analysis
import os

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "Image manquante"}), 400
    
    image_file = request.files["image"]
    filename = image_file.filename
    image_path = os.path.join("uploads", filename)

    # Créer dossier uploads si inexistant
    os.makedirs("uploads", exist_ok=True)

    image_file.save(image_path)

    # Appeler la fonction d'analyse (OpenAI + génération audio)
    description, audio_path = analyze_image(image_path)

    # Enregistrer dans MongoDB
    record = {
        "filename": filename,
        "description": description,
        "audio_file": audio_path
    }
    insert_analysis(record)

    return jsonify({
        "description": description,
        "audio_file": audio_path
    })
