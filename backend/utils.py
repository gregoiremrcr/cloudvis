import base64
from PIL import Image
from io import BytesIO
from gtts import gTTS

def image_to_base64(image_path):
    image = Image.open(image_path).convert("RGB")
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def texte_en_audio(texte, langue="fr", output_path="description.mp3"):
    tts = gTTS(text=texte, lang=langue)
    tts.save(output_path)
    return output_path
