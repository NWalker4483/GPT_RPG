import cv2
import numpy as np

class Entity:
	def __init__(self, pos, img, mask, layer):
		self.pos = pos;
		self.img = img
		self.mask = mask;
		self.layer = layer;
		self.minimap_color = None;

	def draw(self, tile_img):
		# resize to the tile
		h,w = tile_img.shape[:2];
		img = cv2.resize(self.img, (w,h));
		mask = cv2.resize(self.mask, (w,h));

		# DEBUG DEBUG DEBUG
		# print("Img Shape:", img.shape);
		# print("Mask Shape:", mask.shape);
		# print("Tile Shape:", tile_img.shape);

		# combined_img = cv2.bitwise_and(tile_img, img, mask=mask);
		# tile_img[:] = combined_img;
		# cv2.imshow("Tile Image", tile_img);
		# cv2.waitKey(0);
		# tile_img[mask==255] = img;

		tile_img[np.where(mask == 255)] = img[np.where(mask == 255)]

