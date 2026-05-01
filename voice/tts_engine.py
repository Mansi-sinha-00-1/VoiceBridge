def generate_voice(text, tone="normal", language="en"):
    import os
    import uuid
    from gtts import gTTS

    os.makedirs("media/audio", exist_ok=True)

    filename = f"{uuid.uuid4()}.mp3"
    full_path = os.path.join("media", "audio", filename)
    relative_path = os.path.join("audio", filename)

    # 🎯 Tone handling
    if tone == "slow":
        slow = True
    elif tone == "fast":
        slow = False
        text = text.upper() + "!"
    else:
        slow = False

    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(full_path)

    return relative_path