# generate_videos.py
import os
import random
from pytrends.request import TrendReq
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
import subprocess

# Prepare folders
os.makedirs("output/scripts", exist_ok=True)
os.makedirs("output/audio", exist_ok=True)
os.makedirs("output/images", exist_ok=True)
os.makedirs("output/video", exist_ok=True)

# Trending topics
topics = ["AI tools","Tech hacks","Smart websites","Automation","AI apps"]
pytrends = TrendReq(hl='en-US', tz=0)

for i in range(1, 91):
    print(f"=== Generating video {i} ===")

    # 1️⃣ Trending keyword
    keyword = topics[i % len(topics)]
    with open(f"output/scripts/script_{i:02d}.txt", "w") as f:
        f.write(keyword)

    # 2️⃣ Generate script
    hooks = [
        f"Did you know about {keyword}?",
        f"This {keyword} will blow your mind!",
        f"Stop scrolling! You need to see this {keyword}.",
        f"Quick tip about {keyword} you can't miss!"
    ]
    bodies = [
        f"{keyword} can save you so much time.",
        f"Here’s a quick hack using {keyword}.",
        f"Use {keyword} to level up your workflow.",
        f"This simple {keyword} trick boosts productivity."
    ]
    closes = ["Try it now!", "Don't forget to share!", "Hit follow for more!", "Implement this today!"]
    script_text = f"{random.choice(hooks)}\n{random.choice(bodies)}\n{random.choice(closes)}"
    with open(f"output/scripts/processed_script_{i:02d}.txt","w") as f:
        f.write(script_text)

    # 3️⃣ Voiceover
    tts = gTTS(text=script_text, lang='en')
    tts.save(f"output/audio/audio_{i:02d}.mp3")

    # 4️⃣ Background image
    img = Image.new("RGB",(1080,1920),(30,30,30))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
    text = f"Video {i:02d} - AI Shorts"

    # ✅ Fix for Pillow textsize
    if hasattr(draw, "textbbox"):
        bbox = draw.textbbox((0,0), text, font=font)
        w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    else:
        w, h = draw.textsize(text, font=font)

    draw.text(((1080-w)/2,(1920-h)/2), text, font=font, fill=(255,255,255))
    img.save(f"output/images/image_{i:02d}.png")

    # 5️⃣ Combine into video
    subprocess.run([
        "ffmpeg", "-loop", "1",
        "-i", f"output/images/image_{i:02d}.png",
        "-i", f"output/audio/audio_{i:02d}.mp3",
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p", "-shortest",
        "-y", f"output/video/video_{i:02d}.mp4"
    ])
