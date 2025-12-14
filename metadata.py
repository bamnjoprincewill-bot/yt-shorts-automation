import random

hashtags = [
    "#aitools", "#techhacks", "#aiwebsites",
    "#productivity", "#makemoneyonline",
    "#shorts", "#youtubeshorts", "#ai"
]

with open("topics.txt") as f:
    topics = f.readlines()

with open("links.txt") as f:
    links = f.readlines()

titles = []
descriptions = []

for i, topic in enumerate(topics):
    title = f"This AI Tool Is Going Viral 😳 ({topic.strip()})"
    link = random.choice(links).strip()

    description = f"""
This AI tool is trending everywhere.
People are using it to save time and work smarter.

👉 Try it here: {link}

{' '.join(random.sample(hashtags, 5))}
"""

    titles.append(title)
    descriptions.append(description)

with open("metadata.txt", "w") as f:
    for t, d in zip(titles, descriptions):
        f.write(t + "\n")
        f.write(d + "\n---\n")

