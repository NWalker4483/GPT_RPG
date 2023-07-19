import os
import cv2
import random
import numpy as np

# colors = {
# 	"water_blue" : (195, 105, 39),
# 	"rock_blue" : (156, 113, 87),
# 	"dark_grass" : (81, 152, 107),
# }
colors = [(195, 105, 39), (156, 113, 87), (81, 152, 107)];

# make blur
def blurRegion(size=50):
	blank = np.zeros((size,size,3), np.uint8);
	for y in range(size):
		for x in range(size):
			color = random.choice(colors);
			blank[y][x] = color;

	# blur
	blank = cv2.GaussianBlur(blank, (5,5), 0);
	return blank;
blur = blurRegion();

# load files
folder = "GrassCopy/";
files = os.listdir(folder);

for file in files:
	# get image and mask
	img = cv2.imread(folder + file);
	mask = cv2.inRange(img, (120,120,120), (255,255,255), cv2.THRESH_BINARY);
	# img[mask==255] = (195, 105, 39); # water blue
	# img[mask==255] = (156, 113, 87); # rock blue

	# swap pixels
	pos = np.where(mask==255);
	for ind in range(len(pos[0])):
		y = pos[0][ind];
		x = pos[1][ind];
		rx = random.randint(0,49);
		ry = random.randint(0,49);
		img[y][x] = blur[ry][rx];


	cv2.imwrite(folder + file, img);