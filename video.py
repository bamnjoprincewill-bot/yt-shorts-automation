import os
from moviepy.editor import *

os.makedirs("output", exist_ok=True)

for i in range(30):
    audio = AudioFileClip(f"audio/voice_{i}.mp3")

    bg = ColorClip(
        size=(1080,1920),
        color=(0,0,0),
        duration=audio.duration
    )

    video = bg.set_audio(audio)

    video.write_videofile(
        f"output/short_{i}.mp4",
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )
