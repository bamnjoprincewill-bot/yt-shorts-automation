# trends.py
# SAFE trending system (NO Google, NO bans)

import random

# High-viral evergreen niches for Shorts
TRENDING_POOLS = [
    "AI tools you didn’t know exist",
    "Websites that feel illegal to know",
    "AI websites that save hours",
    "Tech hacks that feel unreal",
    "Free AI tools smarter than ChatGPT",
    "Hidden websites on the internet",
    "AI tools students should use",
    "Websites that do the work for you",
    "AI tools that feel like cheating",
    "Smart websites nobody talks about"
]

# Pick 3 daily ideas
daily_topics = random.sample(TRENDING_POOLS, 3)

with open("topics.txt", "w") as f:
    for topic in daily_topics:
        f.write(topic + "\n")

print("✅ Topics generated successfully")
