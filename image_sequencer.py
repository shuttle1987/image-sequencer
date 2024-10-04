"""Small script to make video files from a sequence of image files"""

import argparse
from pathlib import Path
import moviepy.video.io.ImageSequenceClip

parser = argparse.ArgumentParser(description='Process image files into a video')
parser.add_argument("--fps", type=float, help="How many frames per second", default=1)
args = parser.parse_args()

image_folder: Path = Path('test')
fps: float = args.fps

image_files = [str(img) for img in image_folder.glob("*.png")]

print(image_files)
image_files.sort()
print(image_files)

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('my_video.mp4')
