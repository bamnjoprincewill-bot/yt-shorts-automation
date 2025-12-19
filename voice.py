import argparse
from gtts import gTTS
import os

# Parse video number from workflow
parser = argparse.ArgumentParser()
parser.add_argument("--video-number", type=int, required=True)
args = parser.parse_args()
video_number = args.video_number

# Example: replace this with your actual script text for each video
script_text = f"This is your script for video number {video_number}"

# Generate TTS audio
tts = gTTS(text=script_text, lang='en')
os.makedirs("output/audio", exist_ok=True)
audio_path = f"output/audio/audio_{video_number:02d}.mp3"
tts.save(audio_path)

print(f"[✅] TTS audio generated: {audio_path}")
