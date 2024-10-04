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
usage: image_sequencer.py [-h] [--fps FPS] [--output OUTPUT] [--input INPUT] [--stringsort]

Process image files into a video.

optional arguments:
  -h, --help       show this help message and exit
  --fps FPS        How many frames per second
  --output OUTPUT  Output filename
  --input INPUT    Input directory
  --stringsort     Sort filenames based on string values rather than integers.

```

## Note on how filenames are sorted

By default filenames sort based on the numbers in them instead of sorting on the strings. Imagine you had a number of files like `1.png`, `2.png`, `3.png`.... `12.png` in `test` directory. In this case sorting with natural sort gives you the following order of images in the output video:

```
$ python image_sequencer.py --fps 1  --input test --output testsorting.mp4
Found 12 images to process
[PosixPath('test/8.png'), PosixPath('test/10.png'), PosixPath('test/5.png'), PosixPath('test/9.png'), PosixPath('test/3.png'), PosixPath('test/1.png'), PosixPath('test/12.png'), PosixPath('test/2.png'), PosixPath('test/11.png'), PosixPath('test/4.png'), PosixPath('test/7.png'), PosixPath('test/6.png')]
Sorting images...
['test/1.png', 'test/2.png', 'test/3.png', 'test/4.png', 'test/5.png', 'test/6.png', 'test/7.png', 'test/8.png', 'test/9.png', 'test/10.png', 'test/11.png', 'test/12.png']
Moviepy - Building video testsorting.mp4.
Moviepy - Writing video testsorting.mp4

Moviepy - Done !                                                                                                                                                            
Moviepy - video ready testsorting.mp4
```

But you can sort based on the strings values for the filenames if you want, but if you have numbers you'll see an ordering that might not be what you expect:

```
$ python image_sequencer.py --fps 1 --stringsort --input test --output testsorting.mp4
Found 12 images to process
[PosixPath('test/8.png'), PosixPath('test/10.png'), PosixPath('test/5.png'), PosixPath('test/9.png'), PosixPath('test/3.png'), PosixPath('test/1.png'), PosixPath('test/12.png'), PosixPath('test/2.png'), PosixPath('test/11.png'), PosixPath('test/4.png'), PosixPath('test/7.png'), PosixPath('test/6.png')]
Sorting images...
Warning natural integer sorting is not being used, numbers may sort in strange order
['test/1.png', 'test/10.png', 'test/11.png', 'test/12.png', 'test/2.png', 'test/3.png', 'test/4.png', 'test/5.png', 'test/6.png', 'test/7.png', 'test/8.png', 'test/9.png']
Moviepy - Building video testsorting.mp4.
Moviepy - Writing video testsorting.mp4

Moviepy - Done !                                                                                                                                                            
Moviepy - video ready testsorting.mp4
```