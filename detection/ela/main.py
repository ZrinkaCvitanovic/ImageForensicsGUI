#importing libs
#source: https://github.com/z1311/Image-Manipulation-Detection/blob/master/ela.py
from PIL import ImageChops
import PIL.Image
import os
import argparse

def ELA(img_path, q):
        DIR = "temp/"
        TEMP = "temp/tmp.jpg"
        SCALE = 10
        original = PIL.Image.open(img_path)
        if(os.path.isdir(DIR) == False):
                os.mkdir(DIR)
        original.save(TEMP, quality=q)
        temporary = PIL.Image.open(TEMP)
        diff = ImageChops.difference(original, temporary)
        d = diff.load()
        WIDTH, HEIGHT = diff.size
        for x in range(WIDTH):
                for y in range(HEIGHT):
                        d[x, y] = tuple(k * SCALE for k in d[x, y])

        diff.save(img_path + "_ela_" + str(q) + ".jpg")
        os.remove(TEMP)
        os.rmdir("temp")

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str, help='path to input image')
parser.add_argument('quality', type=int, help='desired quality')
args = parser.parse_args()

ELA(args.in_path, args.quality)
