import cv2
import numpy as np

# creates an image hash
def getImageHash(tile):
	gray = cv2.cvtColor(tile, cv2.COLOR_BGR2GRAY);
	hashstr = "";
	h,w = gray.shape[:2];
	for y in range(h):
		for x in range(w):
			hashstr += str(gray[y][x]);
	return hashstr;

# check if tile is all white
def isBlank(tile):
	gray = cv2.cvtColor(tile, cv2.COLOR_BGR2GRAY);
	mask = cv2.inRange(gray, 250, 255, cv2.THRESH_BINARY);
	mask = cv2.bitwise_not(mask);

	# gray = cv2.resize(gray, (200,200));
	# mask = cv2.resize(mask, (200,200));
	# cv2.imshow("Gray", gray);
	# cv2.imshow("Mask", mask);
	# cv2.waitKey(1);
	return np.sum(mask) == 0;

# list of spritesheets
sheets = ["grass_crop.png"];

# keep track of duplicates
dupes = {};

filenum = 0;
for sheet in sheets:

	# sprite atlas
	atlas = cv2.imread(sheet);
	sprite_size = 16;

	# resize target
	scale = 4;
	target_size = int(sprite_size * scale);

	# chop it up
	output_dir = "Atlas/";
	height, width = atlas.shape[:2];
	ytiles = int(height / sprite_size);
	xtiles = int(width / sprite_size);
	for y in range(ytiles):
		sy = y * sprite_size;
		ey = sy + sprite_size;
		for x in range(xtiles):
			sx = x * sprite_size;
			ex = sx + sprite_size;

			# crop
			print("Pos: ", (sx,sy));
			tile = atlas[sy:ey,sx:ex];

			# blank check
			# if isBlank(tile):
			# 	continue;

			# dupe check
			# hashed = getImageHash(tile);
			# if hashed in dupes:
			# 	continue;
			# dupes[hashed] = True;

			# resize
			tile = cv2.resize(tile, (target_size,target_size), interpolation=cv2.INTER_NEAREST);

			# create filename
			filename = output_dir + str(filenum).zfill(3) + ".png";
			filenum += 1;
			print("Filename: ", filename);
			cv2.imwrite(filename, tile);


