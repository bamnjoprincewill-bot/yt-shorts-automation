import os

os.makedirs("meta", exist_ok=True)

for i in range(5):
    with open(f"meta/title_{i}.txt", "w") as f:
        f.write("Discipline Will Change Your Life #shorts")
