# image_utils.py

import base64
from PIL import Image
from io import BytesIO
import openai
from gtts import gTTS
from dotenv import load_dotenv
import os

# Charger les variables d’environnement depuis le fichier .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def image_to_base64(image_path):
    image = Image.open(image_path).convert("RGB")
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def analyser_image(image_path, prompt_user="Décris cette image."):
    img_b64 = image_to_base64(image_path)
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tu es un assistant spécialisé dans l’accessibilité pour les personnes aveugles. "
                                          "Ton rôle est de décrire précisément le contenu d’une image : les objets visibles, "
                                          "les personnes, les expressions, les couleurs dominantes, les émotions dégagées, "
                                          "le contexte possible (famille, vacances, musée, art, etc.), et l’ambiance générale. "
                                          "Utilise un langage clair, riche, imagé, mais accessible. "
                                          "Ne fais pas d’hypothèses non fondées et n’invente rien qui ne semble pas visible sur l’image. "
                                          "Ton objectif est de permettre à une personne aveugle de se représenter mentalement la scène. "
                                          "La description doit être complète, fluide, et d’une durée d’écoute raisonnable (environ 1 à 2 minutes à l’oral)."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_user},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
                ]
            }
        ]
    )
    return response['choices'][0]['message']['content']

def texte_en_audio(texte, langue='fr', fichier_sortie="description.mp3"):
    tts = gTTS(text=texte, lang=langue)
    tts.save(fichier_sortie)
    return fichier_sortie
