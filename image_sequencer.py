"""Small script to make video files from a sequence of image files"""

from pathlib import Path
import moviepy.video.io.ImageSequenceClip

image_folder: Path = Path('test')
fps: int = 1

image_files = [str(img) for img in image_folder.glob("*.png")]

print(image_files)
image_files.sort()
print(image_files)

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('my_video.mp4')
