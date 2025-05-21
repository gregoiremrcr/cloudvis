from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

from routes.analyze import analyze_bp
from routes.history import history_bp

app.register_blueprint(analyze_bp, url_prefix="/analyze")
app.register_blueprint(history_bp, url_prefix="/history")

@app.route("/")
def home():
    return "Bienvenue sur le backend CloudVision !"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)
