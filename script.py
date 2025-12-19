import os

os.makedirs("scripts", exist_ok=True)

with open("topics.txt") as f:
    topics = f.readlines()

for i in range(5):
    text = f"{topics[i % len(topics)].strip()}\nStay hard. Keep going."
    with open(f"scripts/script_{i}.txt", "w") as s:
        s.write(text)
