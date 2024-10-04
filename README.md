# image-sequencer

A small script to make a video from a sequence of images

## Install

Make sure you have Python3 installed on your computer (this script was tested with Python3.9)

Create a virtual environment
```
python3 -m venv venv
```

Activate your virtual environment, eg on linux:

```
source venv/bin/activate
```

update pip

```
python3 -m pip install -U pip
```

Install dependencies

```
python3 -m pip install -r requirements.txt
```

## Example usage

Invoke the script with the parameters you want:

```
python image_sequencer.py --fps 10 --input my_images_directory --output my_video.mp4
```

You can also see the help for other information:

```
$ python image_sequencer.py --help
usage: image_sequencer.py [-h] [--fps FPS] [--output OUTPUT] [--input INPUT] [--naturalsort NATURALSORT]

Process image files into a video.

optional arguments:
  -h, --help            show this help message and exit
  --fps FPS             How many frames per second
  --output OUTPUT       Output filename
  --input INPUT         Input directory
  --naturalsort NATURALSORT
                        Sort integers in filenames naturally instead of using string sorting.
```
