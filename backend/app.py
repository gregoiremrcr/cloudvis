# backend/app.py

import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from image_utils import analyser_image, texte_en_audio
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)  # Autorise les requêtes du frontend

UPLOAD_FOLDER = "uploads"
AUDIO_FOLDER = "audio"
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "Aucune image transmise."}), 400

    file = request.files['image']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({"error": "Fichier invalide."}), 400

    filename = secure_filename(file.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(image_path)

    # Analyse + audio
    description = analyser_image(image_path)
    audio_filename = filename.rsplit('.', 1)[0] + ".mp3"
    audio_path = os.path.join(AUDIO_FOLDER, audio_filename)
    texte_en_audio(description, fichier_sortie=audio_path)

    return jsonify({
        "description": description,
        "audio_url": f"/audio/{audio_filename}"
    })

@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
