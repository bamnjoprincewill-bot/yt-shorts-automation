import os

for i in range(3):
    os.system(
        f'whisper voice_{i}.wav --model small --output_format srt'
    )
