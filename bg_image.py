import argparse
from PIL import Image, ImageDraw, ImageFont
import os

# Parse video number
parser = argparse.ArgumentParser()
parser.add_argument("--video-number", type=int, required=True)
args = parser.parse_args()
video_number = args.video_number

# Create output folder
os.makedirs("output/images", exist_ok=True)

# Create a simple background image (1080x1920 for Shorts)
img = Image.new("RGB", (1080, 1920), color=(30, 30, 30))
draw = ImageDraw.Draw(img)

# Add sample text (replace with actual content if needed)
font_size = 80
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    font = ImageFont.load_default()

text = f"Video {video_number:02d} - AI Shorts"
text_w, text_h = draw.textsize(text, font=font)
draw.text(
    ((1080 - text_w) / 2, (1920 - text_h) / 2),
    text,
    font=font,
    fill=(255, 255, 255)
)

# Save image
img_path = f"output/images/image_{video_number:02d}.png"
img.save(img_path)
print(f"[✅] Background image generated: {img_path}")
