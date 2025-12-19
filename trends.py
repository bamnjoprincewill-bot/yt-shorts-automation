import argparse
from pytrends.request import TrendReq
import os

# Parse video number
parser = argparse.ArgumentParser()
parser.add_argument("--video-number", type=int, required=True)
args = parser.parse_args()
video_number = args.video_number

# Connect to Google Trends
pytrends = TrendReq(hl='en-US', tz=0)

# Example: choose a popular tech-related keyword for each video
kw_list = ["AI tools", "Tech hacks", "Smart websites", "Automation", "AI apps"]
keyword = kw_list[video_number % len(kw_list)]  # rotate through list

# Save the keyword to a file (used by script.py)
os.makedirs("output/scripts", exist_ok=True)
script_path = f"output/scripts/script_{video_number:02d}.txt"
with open(script_path, "w") as f:
    f.write(f"This is a short video about {keyword}.\nKeep watching to learn more!")

print(f"[✅] Script for video {video_number:02d} saved: {script_path}")
