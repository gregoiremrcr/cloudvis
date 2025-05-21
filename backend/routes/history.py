from flask import Blueprint, jsonify
from models.analysis_model import get_all_analyses

history_bp = Blueprint("history", __name__)

@history_bp.route("/", methods=["GET"])
def history():
    analyses = get_all_analyses()

    # Convertir ObjectId et datetime en string si besoin
    for a in analyses:
        a["_id"] = str(a["_id"])
        a["timestamp"] = a["timestamp"].isoformat()

    return jsonify(analyses)
