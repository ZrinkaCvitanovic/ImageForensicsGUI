#!/usr/bin/env python3
#source: https://github.com/olvb/pyheal
import argparse
import pyheal
import imageio

parser = argparse.ArgumentParser()
parser.add_argument('in_path', metavar='input_img', type=str,
	 				help='path to input image')
parser.add_argument('mask_path', metavar='mask_img', type=str,
					help='path to mask image')
parser.add_argument('-r', '--radius', metavar='R', nargs=1, type=int, default=[5],
					help='neighborhood radius')
args = parser.parse_args()

img = imageio.v2.imread(args.in_path)
remove_ext = args.in_path.split(".")
real_path = remove_ext[0]
extension = "." + remove_ext[1]

out_path = real_path + "-Telea"  + extension
mask_img = imageio.v2.imread(args.mask_path)
mask = mask_img[:, :, 0].astype(bool, copy=False)
pyheal.inpaint(img, mask, args.radius[0])
imageio.v2.imwrite(out_path, img)
