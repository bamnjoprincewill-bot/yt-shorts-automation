
def script(topic):
    return f"""
Stop scrolling.
This AI tool is exploding right now.
{topic} helps people save hours every day.
Most people don’t know this exists yet.
Link is in the description.
"""

with open("topics.txt") as f:
    topics = f.readlines()

with open("scripts.txt", "w") as f:
    for t in topics:
        f.write(script(t.strip()) + "\n---\n")
