import os
from gtts import gTTS

os.makedirs("audio", exist_ok=True)

for i in range(5):
    with open(f"scripts/script_{i}.txt") as f:
        text = f.read()

    tts = gTTS(text)
    tts.save(f"audio/voice_{i}.mp3")
