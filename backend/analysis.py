import openai
import os
from utils import image_to_base64, texte_en_audio

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_image(image_path):
    img_b64 = image_to_base64(image_path)

    messages = [
        {"role": "system", "content": (
            "Tu es un assistant spécialisé dans l’accessibilité pour les personnes aveugles. "
            "Décris précisément le contenu de cette image : objets, personnes, couleurs, expressions, "
            "émotions, contexte, ambiance. Utilise un langage clair et imagé. "
            "Ne fais aucune hypothèse non fondée."
        )},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Décris cette image."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
            ]
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )

    description = response['choices'][0]['message']['content']

    # Génération audio
    audio_path = image_path.rsplit(".",1)[0] + "_description.mp3"
    texte_en_audio(description, output_path=audio_path)

    return description, audio_path
