# 📸 CloudVision

**CloudVision** est une plateforme web fullstack qui permet aux utilisateurs d’uploader des images, puis de les faire analyser automatiquement par une intelligence artificielle. Le projet combine le développement Python (Flask) avec une interface React, le tout déployé via Docker sur une infrastructure cloud. L’analyse d’image est assurée par **GPT-4 Vision (OpenAI)** et peut être enrichie par **OpenCV** pour certains traitements bas-niveau.

---

## 🚀 Objectifs pédagogiques

- Comprendre l’intégration d’un backend Python avec une API d’IA.
- Apprendre à construire une application React connectée à une API Flask.
- Maîtriser Docker pour le déploiement multi-conteneurs.
- Manipuler des images et appliquer une analyse IA.
- Gérer une base de données NoSQL (MongoDB).
- Organiser et livrer un projet structuré (infra & dev).

---

## 🧰 Stack technique

| Composant        | Technologie utilisée              |
|------------------|-----------------------------------|
| Backend API      | Python + Flask                    |
| Frontend         | React.js                          |
| Base de données  | MongoDB                           |
| Analyse IA       | OpenAI API (GPT-4 Vision)         |
| Traitement image | OpenCV (en local, prétraitement)  |
| Conteneurisation | Docker + Docker Compose           |
| Déploiement      | Cloud provider (GCP, AWS, etc.)   |

---

## 🖼️ Fonctionnalités

- ✅ Upload d’images via l’interface web
- ✅ Analyse automatique par GPT-4 Vision (description, OCR, etc.)
- ✅ Stockage des résultats dans MongoDB
- ✅ Affichage des résultats d’analyse dans l’interface React
- ✅ Traitement optionnel avec OpenCV (recadrage, prétraitement, etc.)
- ✅ Interface simple, responsive et pédagogique

---

## 🏗️ Architecture du projet

cloudvision/
│
├── backend/ # API Flask + OpenAI + MongoDB
│ ├── app.py
│ ├── analysis.py # Appels à GPT-4 Vision
│ ├── image_utils.py # Fonctions OpenCV
│ └── requirements.txt
│
├── frontend/ # App React
│ ├── src/
│ └── package.json
│
├── docker-compose.yml # Configuration multi-conteneur
├── README.md
└── .env # Variables d’environnement (API keys, etc.)


---

## 🔐 Prérequis

- Compte OpenAI avec accès à GPT-4 Vision
- Docker & Docker Compose
- Accès cloud (GCP, AWS, etc.)
- Node.js / npm
- Python 3.10+

---

## ⚙️ Installation & Lancement

1. **Cloner le dépôt :**

```bash
git clone https://github.com/votre-utilisateur/cloudvision.git
cd cloudvision

    Configurer les variables d’environnement :

Créer un fichier .env à la racine avec :

OPENAI_API_KEY=sk-xxxxxx
MONGODB_URI=mongodb://mongodb:27017/cloudvision

    Démarrer l’application avec Docker :

docker-compose up --build

    Accédez à l’app :
    Frontend → http://localhost:3000
    Backend API → http://localhost:5000/api

📩 Exemple d’appel à l’API (analyse image)

POST /api/analyze-image
Content-Type: multipart/form-data
Body: image file (.jpg, .png, etc.)

Réponse :

{
  "description": "Une photo représentant un chat noir sur un canapé.",
  "text_detected": "Coca-Cola",
  "objects": ["chat", "canapé"]
}

🧠 Améliorations possibles

    Authentification utilisateur (Auth0, Firebase)

    File de traitement (Celery + Redis)

    Historique des analyses

    Visualisation d’analyse (ex : surlignage OCR)

    Support multi-langues

📜 Licence

Projet réalisé dans un cadre pédagogique. Reproduction ou réutilisation soumise à autorisation.


---

Souhaitez-vous aussi :
- Un **exemple de `.env` complet** ?
- Une **doc Swagger/OpenAPI de l’API Flask** ?
- Un **modèle de rapport de soutenance** lié à ce projet ?