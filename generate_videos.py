# generate_high_quality_videos.py
import os
import random
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
import subprocess
import zipfile

# --------------------------
# 1️⃣ Setup folders
# --------------------------
os.makedirs("output/scripts", exist_ok=True)
os.makedirs("output/audio", exist_ok=True)
os.makedirs("output/images", exist_ok=True)
os.makedirs("output/video", exist_ok=True)
os.makedirs("output/metadata", exist_ok=True)

# --------------------------
# 2️⃣ Define topics (real tech/AI tips)
# --------------------------
topics = [
    {"title": "ChatGPT", "tip": "Generate content instantly, including articles, emails, and code."},
    {"title": "Canva", "tip": "Design graphics quickly using templates and AI features."},
    {"title": "MidJourney", "tip": "Create AI images in seconds for your projects."},
    {"title": "Zapier", "tip": "Automate repetitive tasks and save hours every day."},
    {"title": "Notion", "tip": "Organize projects, notes, and workflows efficiently."},
    {"title": "Grammarly", "tip": "Correct writing instantly and improve clarity."},
    {"title": "DALL-E", "tip": "Generate unique AI images with prompts quickly."},
    {"title": "Trello", "tip": "Manage tasks and collaborate easily with your team."}
]

hashtags = "#AI #TechTips #Automation #Shorts"

# --------------------------
# 3️⃣ Generate videos
# --------------------------
for i in range(1, 91):
    print(f"=== Generating video {i} ===")

    # Pick a random topic
    topic = random.choice(topics)
    title = topic["title"]
    tip = topic["tip"]

    # Create Hook, Body, Close
    hooks = [
        f"Stop scrolling! Check out {title}!",
        f"Did you know about {title}?",
        f"This {title} will blow your mind!"
    ]
    bodies = [
        f"{tip}. Try it today!",
        f"Boost your workflow with {title}: {tip}.",
        f"Here’s a quick hack using {title}: {tip}."
    ]
    closes = [
        "Hit follow for more!",
        "Try this now!",
        "Share with your friends!"
    ]

    script_text = f"{random.choice(hooks)}\n{random.choice(bodies)}\n{random.choice(closes)}"

    # Save script
    script_file = f"output/scripts/script_{i:02d}.txt"
    with open(script_file, "w") as f:
        f.write(script_text)

    # --------------------------
    # Generate voiceover
    # --------------------------
    audio_file = f"output/audio/audio_{i:02d}.mp3"
    tts = gTTS(text=script_text, lang='en')
    tts.save(audio_file)

    # --------------------------
    # Generate background image with overlay text
    # --------------------------
    img = Image.new("RGB", (1080,1920), (20,20,20))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()

    lines = script_text.split("\n")
    y_offset = 400
    for line in lines:
        if hasattr(draw,"textbbox"):
            bbox = draw.textbbox((0,0), line, font=font)
            w,h = bbox[2]-bbox[0], bbox[3]-bbox[1]
        else:
            w,h = draw.textsize(line,font=font)
        draw.text(((1080-w)/2, y_offset), line, font=font, fill=(255,255,255))
        y_offset += h + 50

    image_file = f"output/images/image_{i:02d}.png"
    img.save(image_file)

    # --------------------------
    # Generate SRT captions
    # --------------------------
    srt_file = f"output/video/video_{i:02d}.srt"
    with open(srt_file, "w") as srt:
        start = 0.0
        for idx, line in enumerate(lines, 1):
            duration = 3 if idx==1 else 10 if idx==2 else 2
            end = start + duration
            srt.write(f"{idx}\n")
            srt.write(f"00:00:{int(start):02d},000 --> 00:00:{int(end):02d},000\n")
            srt.write(f"{line}\n\n")
            start = end

    # --------------------------
    # Create video with FFmpeg
    # --------------------------
    video_file = f"output/video/video_{i:02d}.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loop", "1",
        "-i", image_file,
        "-i", audio_file,
        "-vf", f"subtitles={srt_file}:force_style='FontName=Arial,FontSize=60,PrimaryColour=&HFFFFFF&'",
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        video_file
    ])

    # --------------------------
    # Create metadata
    # --------------------------
    metadata_file = f"output/metadata/meta_{i:02d}.txt"
    with open(metadata_file, "w") as f:
        f.write(f"Title: {title} - Quick AI Tip #{i}\n")
        f.write(f"Description: {script_text}\n")
        f.write(f"Hashtags: {hashtags}\n")

# --------------------------
# 4️⃣ Zip all videos for download
# --------------------------
zipf = zipfile.ZipFile("output/all_videos.zip", 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk("output/video"):
    for file in files:
        zipf.write(os.path.join(root, file), file)
zipf.close()

print("✅ All 90 videos generated and zipped in output/all_videos.zip")
