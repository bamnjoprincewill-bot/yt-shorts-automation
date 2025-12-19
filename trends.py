topics = [
    "Discipline beats motivation.",
    "Your future self is watching you.",
    "Nobody is coming to save you.",
    "Work in silence, let success talk.",
    "Comfort kills dreams."
]

with open("topics.txt", "w") as f:
    for t in topics:
        f.write(t + "\n")
