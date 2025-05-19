# analysis.py

import os
from image_utils import analyser_image, texte_en_audio

image_path = "image.jpg"  # Remplace par le chemin de ton image

if not os.path.exists(image_path):
    print("Erreur : Image non trouvée.")
    exit()

# Analyse de l’image
description = analyser_image(image_path)
print("Description générée :\n", description)

# Génération du fichier audio
audio_file = texte_en_audio(description)
print(f"Audio enregistré dans : {audio_file}")
