import cv2
import random
import numpy as np

from item import Dagger, Shield, Sword, Potion
from edge_assembler import tileAssembler

# Tile Images:
# Buch: http://blog-buch.rhcloud.com,
# Jeffrey Kern as committer and creative consultant

class Tile:
	def __init__(self, pos):
		self.pos = pos;
		self.walkable = True;
		self.contains = [];
		self.native_res = [100,100];

		# reserved for special use (player spawns, etc.)
		# to facilitate world gen
		self.reserved = False;

		# space encoding
		self.base_img = None;
		self.encoding = None;

	def setImage(self):
		# imgfile = random.choice(self.atlas.tiles[self.encoding])[1];
		# self.base_img = cv2.imread(imgfile);
		self.base_img = tileAssembler(self.encoding);

	def createImage(self):
		# draw the terrain
		# w,h = self.native_res;
		# img = np.zeros((h,w,3), np.uint8);
		# img[:] = (200,200,200) if self.walkable else (0,0,0);
		img = np.copy(self.base_img);

		# sort the entities by draw layer (low to high)
		self.contains = sorted(self.contains, key=lambda entity: entity.layer); 
		for entity in self.contains:
			entity.draw(img);

		return img;	

	def draw(self, canvas, tile_size):
		# generate
		img = self.createImage();
		img = cv2.resize(img, (tile_size,tile_size));

		# create crop
		sx,sy = self.pos;
		sx *= tile_size;
		sy *= tile_size;
		ex = sx + tile_size;
		ey = sy + tile_size;

		# blit tile
		canvas[sy:ey,sx:ex] = img;

	def manhatDist(self, other_pos):
		dx = other_pos[0] - self.pos[0];
		dy = other_pos[1] - self.pos[1];
		return abs(dx) + abs(dy);

class WorldGrid:
	def __init__(self, width, height):
		# init grid with empty tiles
		self.grid = [];
		self.width = width;
		self.height = height;
		for y in range(self.height):
			row = [];
			for x in range(self.width):
				row.append(Tile((x,y)));
			self.grid.append(row);

		# reserve four corners
		self.grid[0][0].reserved = True;
		self.grid[self.height-1][0].reserved = True;
		self.grid[self.height-1][self.width-1].reserved = True;
		self.grid[0][self.width-1].reserved = True;

	# sets neighbor encoding for each tile
	def setNeighbors(self):
		for y in range(self.height):
			for x in range(self.width):
				# calculate neighbors
				encoding_str = "";
				for py in range(y-1, y+2, 1):
					for px in range(x-1, x+2, 1):
						# check range
						if py < 0 or py >= self.height or px < 0 or px >= self.width:
							encoding_str += "0"
						else:
							encoding_str += "1" if self.grid[py][px].walkable else "0";

				# update encoding
				self.grid[y][x].encoding = encoding_str;
				self.grid[y][x].setImage();


	def numTiles(self):
		return self.width * self.height;

	def getRandomPos(self):
		rx = random.randint(0,self.width-1);
		ry = random.randint(0,self.height-1);
		return [rx,ry];

	def getImage(self, tile_size):
		img_width = self.width * tile_size;
		img_height = self.height * tile_size;
		img = np.zeros((img_height,img_width,3), np.uint8);

		# populate image
		for y in range(self.height):
			for x in range(self.width):
				self.grid[y][x].draw(img, tile_size);
		return img;

	def getMask(self):
		mask = np.zeros((self.height, self.width), np.uint8);
		for y in range(self.height):
			for x in range(self.width):
				mask[y,x] = 255 if self.grid[y][x].walkable else 0;
		return mask;

	def allTilesReachable(self):
		# get mask
		mask = self.getMask();

		# get a seed tile
		seed_pos = None;
		for y in range(self.height):
			for x in range(self.width):
				if self.grid[y][x].walkable:
					seed_pos = (x,y);
					break;
		if seed_pos is None:
			return True;

		# check if floodfill can reach all tiles
		cv2.floodFill(mask, None, seed_pos, 0);
		return np.sum(mask==255) == 0;

	# place an obstacle at position, returns true if successful
	def placeObstacle(self, pos):
		# already has an obstacle
		x,y = pos;
		if not self.grid[y][x].walkable or self.grid[y][x].reserved:
			return False;

		# place an obstacle
		self.grid[y][x].walkable = False;

		# check validity
		if not self.allTilesReachable():
			# undo
			self.grid[y][x].walkable = True;
			return False;
		return True;

	# place random obstacles
	def generateObstacles(self, num_obstacles):
		while num_obstacles > 0:
			rpos = self.getRandomPos();
			if self.placeObstacle(rpos):
				num_obstacles -= 1;
			# print progress
			if num_obstacles % 100 == 0:
				print("Remaining Obstacles: ", num_obstacles);

	# place random items on open tiles
	def generateItems(self, num_items, item_set):
		while num_items > 0:
			x,y = self.getRandomPos();
			if self.grid[y][x].walkable and len(self.grid[y][x].contains) == 0:
				# choose and place an item
				index = random.randint(0,len(item_set)-1);
				self.grid[y][x].contains.append(item_set[index].getCopy(pos=[x,y]));
				num_items -= 1;
    
    def placeItems(self, items):
        pass

if __name__ == "__main__":
	# generate and populate world
	world = WorldGrid(30, 15);
	world.generateObstacles(int(world.numTiles() * 0.20)); # % obstacles
	world.setNeighbors();
	world.generateItems(15, [Dagger((0,0)),Shield((0,0)),Sword((0,0)),Potion((0,0))]);
	world_map = world.getImage(tile_size=50)
	cv2.imshow("Map", world_map)
	cv2.waitKey(0)