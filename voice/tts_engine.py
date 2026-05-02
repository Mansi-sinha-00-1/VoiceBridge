from django.conf import settings
import os
import uuid
from gtts import gTTS

def generate_voice(text, tone="normal", language="en"):
    audio_dir = os.path.join(settings.MEDIA_ROOT, "audio")

    # Ensure directory exists
    os.makedirs(audio_dir, exist_ok=True)

    filename = f"{uuid.uuid4()}.mp3"
    full_path = os.path.join(audio_dir, filename)

    print("Saving file to:", full_path)

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(full_path)

    return f"audio/{filename}"