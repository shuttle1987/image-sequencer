"""Small script to make video files from a sequence of image files"""

import argparse
from pathlib import Path
import moviepy.video.io.ImageSequenceClip

parser = argparse.ArgumentParser(description='Process image files into a video')
parser.add_argument("--fps", type=float, help="How many frames per second", default=1)
parser.add_argument("--output", type=str, help="Output filename", default='my_video.mp4')
parser.add_argument("--input", type=str, help="Input directory", default='input-images')
args = parser.parse_args()


image_folder: Path = Path(args.input)
fps: float = args.fps
output_filename = args.output

image_files = [str(img) for img in image_folder.glob("*.png")]

if not image_files:
    raise ValueError(f"Didn't find any input image files in folder '{image_folder}'... aborting")

print(image_files)
image_files.sort()
print(image_files)

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(output_filename)
