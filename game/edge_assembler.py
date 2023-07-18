import os
import cv2
import random
import numpy as np

# 012
# 345
# 678

def blit(base, edge):
	edge = cv2.imread(edge);

	# convert to mask
	gray = cv2.cvtColor(edge, cv2.COLOR_BGR2GRAY);
	mask = cv2.inRange(gray, 250, 255, cv2.THRESH_BINARY);
	# mask = cv2.bitwise_not(mask);

	# overlay
	fore = cv2.bitwise_or(base, base, mask=mask);
	mask = cv2.bitwise_not(mask);
	back = cv2.bitwise_or(edge, edge, mask=mask);
	base = cv2.bitwise_or(fore, back);
	return base;

def tileAssembler(tile_code):
	# check center
	if tile_code[4] == "0":
		return cv2.imread("Assets/Tiles/Water/000.png");

	# base grass tile
	grass_folder = "Assets/Tiles/Grass/";
	grass_tiles = os.listdir(grass_folder);
	base = cv2.imread(grass_folder + random.choice(grass_tiles));

	# up
	if tile_code[1] == "0":
		base = blit(base, "Assets/Tiles/Edges/top_edge.png");

	# down
	if tile_code[7] == "0":
		base = blit(base, "Assets/Tiles/Edges/bottom_edge.png");

	# left
	if tile_code[3] == "0":
		base = blit(base, "Assets/Tiles/Edges/left_edge.png");

	# right
	if tile_code[5] == "0":
		base = blit(base, "Assets/Tiles/Edges/right_edge.png");
	return base;
