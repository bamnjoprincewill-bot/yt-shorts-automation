
import os

with open("scripts.txt") as f:
    scripts = f.read().split("---")

for i, s in enumerate(scripts):
    s = s.replace("\n", " ")
    os.system(
        f'echo "{s}" | piper --model en_US-lessac-medium.onnx --output_file voice_{i}.wav'
    )
