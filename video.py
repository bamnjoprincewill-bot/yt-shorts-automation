import os
import bg_image  # this ensures bg.jpg is created automatically

for i in range(3):
    os.system(
        f'''
ffmpeg -loop 1 -i bg.jpg -i voice_{i}.wav \
-vf "scale=1080:1920,subtitles=voice_{i}.srt:force_style='Fontsize=48,PrimaryColour=&H00FFFF&,OutlineColour=&H000000&,BorderStyle=3'" \
-c:v libx264 -c:a aac -shortest short_{i}.mp4
'''
    )

