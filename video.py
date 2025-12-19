import argparse
import os
import subprocess

# Parse video number from workflow
parser = argparse.ArgumentParser()
parser.add_argument("--video-number", type=int, required=True)
args = parser.parse_args()
video_number = args.video_number

# Paths
image_path = f"output/images/image_{video_number:02d}.png"  # make sure bg_image.py saves here
audio_path = f"output/audio/audio_{video_number:02d}.mp3"
output_video_path = f"output/video_{video_number:02d}.mp4"

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# ffmpeg command to combine image + audio
# Duration of video = duration of audio
cmd = [
    "ffmpeg",
    "-loop", "1",                # loop the image
    "-i", image_path,            # input image
    "-i", audio_path,            # input audio
    "-c:v", "libx264",
    "-tune", "stillimage",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    "-shortest",                 # stop at audio length
    "-y",                        # overwrite output if exists
    output_video_path
]

subprocess.run(cmd, check=True)
print(f"[✅] Video generated: {output_video_path}")
