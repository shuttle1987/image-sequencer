"""Small script to make video files from a sequence of image files.

Store files for processing with a filename that just contains a number that represents where they will be sequenced."""

import argparse
from pathlib import Path
import moviepy.video.io.ImageSequenceClip

parser = argparse.ArgumentParser(description='Process image files into a video.')
parser.add_argument("--fps", type=float, help="How many frames per second", default=1)
parser.add_argument("--output", type=str, help="Output filename", default='my_video.mp4')
parser.add_argument("--input", type=str, help="Input directory", default='input_images')
parser.add_argument("--stringsort", help="Sort filenames based on string values rather than integers.", action='store_true')

args = parser.parse_args()


def sort_filename_by_number(f_name: Path):
    """Return the integer part of a filename.

    >>> sort_filename_by_number(Path('12.png'))
    >>> 12
    """

    return int(f_name.stem)


image_folder: Path = Path(args.input)
fps: float = args.fps
output_filename = args.output
stringsort: bool = args.stringsort

image_files = [img for img in image_folder.glob("*.png")]

if not image_files:
    raise ValueError(f"Didn't find any input image files in folder '{image_folder}'... aborting")

print(f"Found {len(image_files)} images to process")
print(image_files)

print("Sorting images...")
if stringsort:
    image_files = [str(img) for img in image_folder.glob("*.png")]
    print("Warning natural integer sorting is not being used, numbers may sort in strange order")
    image_files.sort()
else:
    image_files.sort(key=sort_filename_by_number)
    image_files = [str(img) for img in image_files]

print(image_files)

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(output_filename)
