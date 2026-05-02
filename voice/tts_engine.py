from googletrans import Translator
from gtts import gTTS
from django.conf import settings
import os, uuid

def generate_voice(text, language="en", mode="accent"):
    # Step 1: translate only if needed
    if mode == "translate" and language != "en":
        try:
            translator = Translator()
            translated = translator.translate(text, dest=language)
            text = translated.text
            print("Translated text:", text)
        except Exception as e:
            print("Translation error:", e)

    # Step 2: save audio
    audio_dir = os.path.join(settings.MEDIA_ROOT, "audio")
    os.makedirs(audio_dir, exist_ok=True)

    filename = f"{uuid.uuid4()}.mp3"
    full_path = os.path.join(audio_dir, filename)

    tts = gTTS(text=text, lang=language)
    tts.save(full_path)

    return f"audio/{filename}"