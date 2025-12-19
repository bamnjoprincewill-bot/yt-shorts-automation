import argparse
import os
import random

# Parse video number
parser = argparse.ArgumentParser()
parser.add_argument("--video-number", type=int, required=True)
args = parser.parse_args()
video_number = args.video_number

# Read trending topic from trends.py output
script_dir = "output/scripts"
os.makedirs(script_dir, exist_ok=True)
topic_file = f"{script_dir}/script_{video_number:02d}.txt"

with open(topic_file, "r") as f:
    topic = f.read().strip()

# Generate hook, body, close
hooks = [
    f"Did you know about {topic}?",
    f"This {topic} will blow your mind!",
    f"Stop scrolling! You need to see this {topic}.",
    f"Quick tip about {topic} you can’t miss!"
]

bodies = [
    f"{topic} can save you so much time and make things easier.",
    f"Here’s a quick hack using {topic} that anyone can try.",
    f"You can use {topic} to level up your workflow instantly.",
    f"This simple {topic} trick will boost your productivity."
]

closes = [
    "Try it now and thank me later!",
    "Don’t forget to share this tip!",
    "Hit follow for more amazing tech hacks!",
    "Make sure to implement this today!"
]

# Randomly select lines
hook = random.choice(hooks)
body = random.choice(bodies)
close = random.choice(closes)

# Combine into 10–20 second short script
final_script = f"{hook}\n{body}\n{close}"

# Save the processed script back
processed_script_path = f"{script_dir}/processed_script_{video_number:02d}.txt"
with open(processed_script_path, "w") as f:
    f.write(final_script)

print(f"[✅] Processed script generated: {processed_script_path}")
